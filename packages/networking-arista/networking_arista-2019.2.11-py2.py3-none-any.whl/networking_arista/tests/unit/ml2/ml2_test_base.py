# Copyright (c) 2018 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from oslo_log import fixture as log_fixture

import cProfile
from eventlet import queue
import mock
from pstats import Stats

from neutron_lib.api.definitions import l3 as l3_const
from neutron_lib.api.definitions import portbindings
from neutron_lib import constants as n_const
import neutron_lib.context
from neutron_lib.plugins import constants as p_const
from neutron_lib.plugins import directory
from neutron_lib.services.trunk import constants as trunk_const
from oslo_config import cfg

from neutron.api.rpc.handlers import l3_rpc
from neutron.common import utils as common_utils
from neutron.plugins.ml2.drivers import type_vxlan  # noqa
from neutron.tests.common import helpers
from neutron.tests.unit.plugins.ml2 import test_plugin

from networking_arista.common import db_lib
from networking_arista.ml2 import arista_sync
from networking_arista.tests.unit import utils


ENABLE_PROFILER = False
ENABLE_LOGGING = False


class MechTestBase(test_plugin.Ml2PluginV2TestCase):
    """Main test cases for Arista Mechanism driver.

    Tests all mechanism driver APIs supported by Arista Driver. It invokes
    all the APIs as they would be invoked in real world scenarios and
    verifies the functionality.
    """

    _mechanism_drivers = ['arista', 'openvswitch']

    def get_additional_service_plugins(self):
        p = super(MechTestBase, self).get_additional_service_plugins()
        p.update({'trunk_plugin_name': 'trunk'})
        return p

    def setUp(self):
        if ENABLE_LOGGING:
            log_fixture.setlevel.logging.root.setLevel(logging.DEBUG)
            self.useFixture(log_fixture.SetLogLevel(['neutron'],
                                                    logging.DEBUG))
        if ENABLE_PROFILER:
            self.pr = cProfile.Profile()
            self.pr.enable()
        utils.setup_arista_wrapper_config(cfg)
        cfg.CONF.set_override('vni_ranges',
                              ['10000:11000'],
                              group='ml2_type_vxlan')
        super(MechTestBase, self).setUp()
        self.plugin.notifier.port_update = self._mock_port_update
        self.plugin.start_rpc_listeners()
        self.host1 = 'host1'
        self.host2 = 'host2'
        self.host3 = 'host3'
        # Hack to ensure agents report being alive
        cfg.CONF.set_override('agent_down_time', 1000)
        helpers.register_ovs_agent(
            host=self.host1, bridge_mappings={self.physnet: 'br-eth1'})
        helpers.register_ovs_agent(
            host=self.host2, bridge_mappings={self.physnet: 'br-eth1'})
        helpers.register_ovs_agent(
            host=self.host3, bridge_mappings={self.physnet2: 'br-eth1'})
        self.region = 'region'
        self.cvx = utils.MockCvx(self.region)
        self.drv = self.driver.mechanism_manager.mech_drivers['arista'].obj
        # multiprocessing.Queue's get() fails to wake up a thread, swap
        # it out for a LightQueue for testing purposes
        self.drv.provision_queue = queue.LightQueue()
        for worker in self.driver._workers:
            if isinstance(worker, arista_sync.AristaSyncWorker):
                self.ar_sync = worker
                self.ar_sync._rpc = self.cvx
                self.ar_sync.provision_queue = self.drv.provision_queue
            worker.start()
        self.trunk_plugin = directory.get_plugin('trunk')
        self.net_count = 0

    def tearDown(self):
        for worker in self.driver._workers:
            worker.stop()
            worker.wait()
        self.cvx.endpoint_data.clear()
        super(MechTestBase, self).tearDown()
        if ENABLE_PROFILER:
            p = Stats(self.pr)
            p.strip_dirs()
            p.sort_stats('cumtime')
            p.print_stats()

    def _mock_port_update(self, context, port, network_type, segmentation_id,
                          physical_network):
        '''Simulates an L2 agent's response to a port_update notification

        After binding a port, the ML2 plugin notifies all L2 agents of the
        binding so that they can configure the datapath. Once they have
        done so, the call either update_devices_up or update_devices_list
        which brings the port status to ACTIVE. This function simply calls
        update_devices_list in response to a binding without actually doing
        any datapath manipulation.
        '''
        plugin = directory.get_plugin()
        rpc_plugin = plugin.endpoints[0]
        host = port.get(portbindings.HOST_ID)
        agent_id = 'ovs-agent-%s' % host
        vif_type = port.get(portbindings.VIF_TYPE)
        if port.get('device_owner') == trunk_const.TRUNK_SUBPORT_OWNER:
            return
        if vif_type == 'ovs':
            device_list = []
            device_list.append(port['id'])
            if port.get('trunk_details'):
                trunk_rpc = self.trunk_plugin._rpc_backend._skeleton
                for s in port['trunk_details']['sub_ports']:
                    s['trunk_id'] = port['trunk_details']['trunk_id']
                    trunk_rpc.update_subport_bindings(
                        self.context, port['trunk_details']['sub_ports'])
                    device_list.append(s['port_id'])
            devices_dict = {'devices_up': device_list,
                            'agent_id': agent_id,
                            'host': port.get(portbindings.HOST_ID)}

            # This is a hack. When calling update_port_status from the rpc
            # handler, the trunk_details db extension gets a new admin context
            # in order to query the parent port's subports' mac address.
            # Querying within the new context's session seems to somehow
            # invalidate the transaction in update_port_status, which causes
            # the status in the db to remain 'DOWN' in spite of an
            # update_port_[pre/post]commit being sent indicating that the
            # status is 'ACTIVE'. For now, I've found that using the same admin
            # context in all queries resolves the issue. In my testing, this
            # doesn't affect real environments using mysql and seems to be
            # limited to sqlite
            #
            # Additional notes: If there is no transaction in progress when a
            # query in the new context is issued, the update_port_status
            # commit succeeds (ie. comment out the context.session.flush() in
            # update_individual_port_db_status
            with mock.patch.object(neutron_lib.context, 'get_admin_context',
                                   return_value=self.context):
                rpc_plugin.update_device_list(context, **devices_dict)

            if port.get('trunk_details'):
                trunk_rpc = self.trunk_plugin._rpc_backend._skeleton
                trunk_rpc.update_trunk_status(
                    self.context, port['trunk_details']['trunk_id'], 'ACTIVE')
        elif (port.get(portbindings.VNIC_TYPE) == 'normal' and
              vif_type == 'unbound'):
            device_dict = {'agent_id': agent_id,
                           'device': port['id'],
                           'host': port.get(portbindings.HOST_ID)}
            rpc_plugin.update_device_down(context, **device_dict)

    def create_network(self, net_dict):
        net = self.plugin.create_network(self.context, net_dict)
        self.plugin.create_subnet(self.context,
                                  {'subnet':
                                   {'tenant_id': net['tenant_id'],
                                    'name': net['name'],
                                    'network_id': net['id'],
                                    'ip_version': 4,
                                    'cidr': '10.0.%d.0/24' % self.net_count,
                                    'gateway_ip': '10.0.%d.1' % self.net_count,
                                    'allocation_pools': None,
                                    'enable_dhcp': False,
                                    'dns_nameservers': None,
                                    'host_routes': None}})
        self.net_count += 1
        n_ctxs = self.plugin.get_network_contexts(self.context, [net['id']])
        return net, n_ctxs[net['id']]

    def delete_network(self, net_id):
        self.plugin.delete_network(self.context, net_id)

    def create_port(self, port_dict):
        minimal_port = {'port':
                        {'name': port_dict.get('name'),
                         'tenant_id': port_dict.get('tenant_id'),
                         'device_id': port_dict.get('device_id'),
                         'fixed_ips': port_dict.get('fixed_ips'),
                         'network_id': port_dict.get('network_id'),
                         'device_owner': '',
                         'admin_state_up': True}}
        port = self.plugin.create_port(self.context, minimal_port)
        full_port = {'port': port_dict}
        port = self.plugin.update_port(self.context, port['id'], full_port)
        p_ctx = self.plugin.get_bound_port_context(self.context, port['id'])
        return port, p_ctx

    def migrate_port(self, port_id, new_host):
        port_dict = {'port': {'binding:host_id': new_host}}
        port = self.plugin.update_port(self.context, port_id, port_dict)
        p_ctx = self.plugin.get_bound_port_context(self.context, port_id)
        return port, p_ctx

    def migrate_dhcp_device(self, port_id, new_device):
        port_dict = {'port':
                     {'device_id': n_const.DEVICE_ID_RESERVED_DHCP_PORT}}
        port = self.plugin.update_port(self.context, port_id, port_dict)
        port_dict = {'port': {'device_id': new_device}}
        port = self.plugin.update_port(self.context, port_id, port_dict)
        p_ctx = self.plugin.get_bound_port_context(self.context, port_id)
        return port, p_ctx

    def bind_trunk_to_host(self, port, device_id, host):
        p_dict = {'port':
                  {'device_owner': n_const.DEVICE_OWNER_COMPUTE_PREFIX,
                   portbindings.HOST_ID: host,
                   'device_id': device_id}}
        port = self.plugin.update_port(self.context, port['id'], p_dict)
        p_ctx = self.plugin.get_bound_port_context(self.context, port['id'])
        return port, p_ctx

    def bind_subport_to_trunk(self, port, trunk):
        parent = self.plugin.get_port(self.context, trunk['port_id'])
        p_dict = {'port':
                  {portbindings.HOST_ID: parent.get(portbindings.HOST_ID),
                   'device_owner': trunk_const.TRUNK_SUBPORT_OWNER}}
        port = self.plugin.update_port(self.context, port['id'], p_dict)
        self.plugin.update_port_status(self.context, port['id'],
                                       n_const.PORT_STATUS_ACTIVE)

    def unbind_port_from_host(self, port_id):
        p_dict = {'port':
                  {portbindings.HOST_ID: None,
                   'device_id': ''}}
        port = self.plugin.update_port(self.context, port_id, p_dict)
        return port

    def bind_trunk_to_baremetal(self, port_id, device_id, host,
                                switch_id, switch_port):
        p_dict = {'port':
                  {'device_id': device_id,
                   'device_owner': n_const.DEVICE_OWNER_BAREMETAL_PREFIX,
                   'binding:host_id': host,
                   'binding:profile': {'local_link_information': [
                       {'switch_id': switch_id,
                        'port_id': switch_port}]},
                   'binding:vnic_type': 'baremetal'}}
        port = self.plugin.update_port(self.context, port_id, p_dict)
        return port

    def unbind_trunk_from_baremetal(self, port_id):
        p_dict = {'port':
                  {'device_id': '',
                   'device_owner': '',
                   'binding:host_id': None,
                   'binding:profile': None,
                   'binding:vnic_type': None,
                   'status': n_const.PORT_STATUS_DOWN,
                   portbindings.VIF_TYPE: portbindings.VIF_TYPE_UNBOUND}}
        self.plugin.update_port(self.context, port_id, p_dict)

    def bind_dvr_to_host(self, port, host):
        p_dict = {'port':
                  {'device_id': port['device_id'],
                   'device_owner': port['device_owner'],
                   portbindings.HOST_ID: host}}
        self.plugin.update_distributed_port_binding(self.context,
                                                    port['id'], p_dict)
        self.plugin.update_port_status(self.context, port['id'],
                                       n_const.PORT_STATUS_ACTIVE,
                                       host)
        p_ctx = self.plugin.get_bound_port_context(self.context, port['id'],
                                                   host)
        return port, p_ctx

    def unbind_dvr_from_host(self, port, host):
        self.plugin.update_port_status(
            self.context, port['id'], n_const.PORT_STATUS_DOWN, host)

    def set_port_to_error_state(self, port):
        self.plugin.update_port_status(
            self.context, port['id'], n_const.PORT_STATUS_ERROR)

    def delete_port(self, port_id):
        self.plugin.delete_port(self.context, port_id)

    def _get_endpoint(self, resource_type):
        endpoint_map = {
            'tenant': 'region/%s/tenant' % self.region,
            'network': 'region/%s/network' % self.region,
            'segment': 'region/%s/segment' % self.region,
            'dhcp': 'region/%s/dhcp' % self.region,
            'router': 'region/%s/router' % self.region,
            'vm': 'region/%s/vm' % self.region,
            'baremetal': 'region/%s/baremetal' % self.region,
            'dhcp_port': 'region/%s/port?type=dhcp' % self.region,
            'router_port': 'region/%s/port?type=router' % self.region,
            'vm_port': 'region/%s/port?type=vm' % self.region,
            'baremetal_port': 'region/%s/port?type=baremetal' % self.region,
            'port_binding': 'region/%s/portbinding' % self.region}
        return endpoint_map[resource_type]

    def _assertResourceCreated(self, resource_type, resource_id):
        endpoint = self._get_endpoint(resource_type)

        def resource_created():
            return resource_id in self.cvx.endpoint_data[endpoint].keys()
        common_utils.wait_until_true(resource_created)

    def _assertResourceDeleted(self, resource_type, resource_id):
        endpoint = self._get_endpoint(resource_type)

        def resource_deleted():
            return resource_id not in self.cvx.endpoint_data[endpoint].keys()
        common_utils.wait_until_true(resource_deleted)

    def assertTenantCreated(self, tenant_id):
        self._assertResourceCreated('tenant', tenant_id)

    def assertTenantDeleted(self, tenant_id):
        self._assertResourceDeleted('tenant', tenant_id)

    def assertNetworkCreated(self, network_id):
        self._assertResourceCreated('network', network_id)

    def assertNetworkDeleted(self, network_id):
        self._assertResourceDeleted('network', network_id)

    def assertSegmentCreated(self, segment_id):
        self._assertResourceCreated('segment', segment_id)

    def assertSegmentDeleted(self, segment_id):
        self._assertResourceDeleted('segment', segment_id)

    def assertDhcpCreated(self, instance_id):
        self._assertResourceCreated('dhcp', instance_id)

    def assertDhcpDeleted(self, instance_id):
        self._assertResourceDeleted('dhcp', instance_id)

    def assertRouterCreated(self, instance_id):
        self._assertResourceCreated('router', instance_id)

    def assertRouterDeleted(self, instance_id):
        self._assertResourceDeleted('router', instance_id)

    def assertVmCreated(self, instance_id):
        self._assertResourceCreated('vm', instance_id)

    def assertVmDeleted(self, instance_id):
        self._assertResourceDeleted('vm', instance_id)

    def assertBaremetalCreated(self, instance_id):
        self._assertResourceCreated('baremetal', instance_id)

    def assertBaremetalDeleted(self, instance_id):
        self._assertResourceDeleted('baremetal', instance_id)

    def assertDhcpPortCreated(self, port_id):
        self._assertResourceCreated('dhcp_port', port_id)

    def assertDhcpPortDeleted(self, port_id):
        self._assertResourceDeleted('dhcp_port', port_id)

    def assertRouterPortCreated(self, port_id):
        self._assertResourceCreated('router_port', port_id)

    def assertRouterPortDeleted(self, port_id):
        self._assertResourceDeleted('router_port', port_id)

    def assertVmPortCreated(self, port_id):
        self._assertResourceCreated('vm_port', port_id)

    def assertVmPortDeleted(self, port_id):
        self._assertResourceDeleted('vm_port', port_id)

    def assertBaremetalPortCreated(self, port_id):
        self._assertResourceCreated('baremetal_port', port_id)

    def assertBaremetalPortDeleted(self, port_id):
        self._assertResourceDeleted('baremetal_port', port_id)

    def assertPortBindingCreated(self, pb_key):
        self._assertResourceCreated('port_binding', pb_key)

    def assertPortBindingDeleted(self, pb_key):
        self._assertResourceDeleted('port_binding', pb_key)


class L3HARouterTestFramework(MechTestBase):

    L3Plugin = ('neutron.services.l3_router.l3_router_plugin.'
                'L3RouterPlugin')

    def get_additional_service_plugins(self):
        p = super(L3HARouterTestFramework,
                  self).get_additional_service_plugins()
        p.update({'flavors_plugin_name': 'neutron.services.flavors.'
                                         'flavors_plugin.FlavorsPlugin'})
        p.update({'l3_plugin_name': self.L3Plugin})
        return p

    def _register_l3_agent(self, host):
        return helpers.register_l3_agent(host=host)

    def setUp(self):
        super(L3HARouterTestFramework, self).setUp()
        self.l3_plugin = directory.get_plugin(p_const.L3)
        self.l3_rpc_cb = l3_rpc.L3RpcCallback()
        self.ext_net = None

    def create_router(self, ha=False, ext_net=None):
        router_dict = {'router': {'name': 'router',
                                  'admin_state_up': True,
                                  'tenant_id': self._tenant_id,
                                  'ha': ha,
                                  'distributed': False}}
        if ext_net:
            router_dict['router'][l3_const.EXTERNAL_GW_INFO] = {'network_id':
                                                                ext_net['id']}
        router = self.l3_plugin.create_router(self.context, router_dict)
        self.l3_plugin.schedule_router(self.context, router['id'])
        for host in self.l3_agents:
            self.sync_routers(router['id'], host['host'])
        return router

    def sync_routers(self, router_id, host):
        """Call to L3 Agent plugin sync_routers

        Since only l3 agent plugin is enabled in the unit test, to get the
        sync data for routers (which causes port update), we need to call the
        l3 agent plugin sync_routers method directly.
        This call is normally done by a process running periodically on
        l3 agent server (neutron-l3-agent).
        """
        self.l3_rpc_cb.sync_routers(self.context, host=host,
                                    router_ids=[router_id])

    def add_router_interface(self, router, interface_info):
        return self.l3_plugin.add_router_interface(self.context, router['id'],
                                                   interface_info)

    def remove_router_interface(self, router, interface_info):
        return self.l3_plugin.remove_router_interface(self.context,
                                                      router['id'],
                                                      interface_info)

    def delete_router(self, router_id):
        return self.l3_plugin.delete_router(self.context, router_id)

    def get_ha_network(self, router):
        networks = [getattr(net, 'Network') for net in db_lib.get_networks()]
        HA_network_name = n_const.HA_NETWORK_NAME % router['project_id']
        net_id = [net.id for net in networks if net.name == HA_network_name]
        return net_id[0]

    def get_network_segments(self, network_id):
        segments = db_lib.get_segments()
        net_segs = [seg.id for seg in segments if seg.network_id == network_id]
        return net_segs

    def update_routers_states(self, router_id, l3_agent):
        binding_l3_agent_host = l3_agent['host']
        binding_l3_agent_id = l3_agent['id']
        self.l3_plugin.update_routers_states(self.context,
                                             {router_id: 'active'},
                                             binding_l3_agent_host)
        bindings = self.l3_plugin.get_ha_router_port_bindings(self.context,
                                                              [router_id])
        binding = [binding for binding in bindings
                   if binding.l3_agent_id == binding_l3_agent_id][0]
        return self.plugin.get_port(self.context, binding.port_id)

    def get_legacy_router_port(self, port_id):
        return self.plugin.get_port(self.context, port_id)

    def assertL3HANetworkCreated(self, router, net_id):
        endpoint = self._get_endpoint('network')
        HA_network_name = n_const.HA_NETWORK_NAME % router['project_id']

        def resource_created():
            cvx_data = self.cvx.endpoint_data[endpoint]
            return (cvx_data and net_id in cvx_data and
                    HA_network_name == cvx_data[net_id]['name'])
        common_utils.wait_until_true(resource_created)

    def assertLegacyRouterCreated(self, router, host):
        endpoint = self._get_endpoint('router')

        def resource_created():
            cvx_data = list(self.cvx.endpoint_data[endpoint].values())
            expected_data = {'hostId': '(see router ports)',
                             'tenantId': router['project_id'],
                             'id': router['id']}
            return cvx_data and cvx_data[0] == expected_data
        common_utils.wait_until_true(resource_created)

    def assertL3HARouterCreated(self, router):
        endpoint = self._get_endpoint('router')

        def resource_created():
            cvx_data = list(self.cvx.endpoint_data[endpoint].values())
            expected_data = {'hostId': '(see router ports)',
                             'tenantId': router['project_id'],
                             'id': router['id']}
            return cvx_data and cvx_data[0] == expected_data
        common_utils.wait_until_true(resource_created)

    def assertL3HAPortCreated(self, router, port_id):
        endpoint = self._get_endpoint('router_port')
        port_name = n_const.HA_PORT_NAME % router['project_id']

        def resource_created():
            cvx_data = self.cvx.endpoint_data[endpoint]
            return (cvx_data and port_id in cvx_data and all(
                [cvx_data[port_id]['tenantId'] == router['project_id'],
                 cvx_data[port_id]['portName'] == port_name,
                 cvx_data[port_id]['instanceId'] == router['id']]))
        common_utils.wait_until_true(resource_created)

    def assertSegmentsCreated(self, segments):
        segment_endpoint = self._get_endpoint('segment')

        def resource_created():
            cvx_segments = self.cvx.endpoint_data[segment_endpoint].keys()
            return cvx_segments and set(cvx_segments) == set(segments)
        common_utils.wait_until_true(resource_created)

    def assertSegmentsDeleted(self, segments):
        segment_endpoint = self._get_endpoint('segment')

        def resource_deleted():
            cvx_data = self.cvx.endpoint_data[segment_endpoint]
            cvx_segments = cvx_data.keys()
            return all(seg not in cvx_segments for seg in segments)
        common_utils.wait_until_true(resource_deleted)

    def assertRouterPortsDeleted(self, ports):
        endpoint = self._get_endpoint('router_port')

        def resource_deleted():
            cvx_data = self.cvx.endpoint_data[endpoint]
            return all(port not in cvx_data for port in ports)
        common_utils.wait_until_true(resource_deleted)
