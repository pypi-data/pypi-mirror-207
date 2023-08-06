# Copyright 2021 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ovsdbapp.backend.ovs_idl import event as row_event


class PortBindingChassisEvent(row_event.RowEvent):
    def __init__(self, bgp_agent, events):
        self.agent = bgp_agent
        table = 'Port_Binding'
        super(PortBindingChassisEvent, self).__init__(
            events, table, None)
        self.event_name = self.__class__.__name__

    def _check_ip_associated(self, mac):
        return len(mac.strip().split(' ')) > 1


class OVNLBMemberEvent(row_event.RowEvent):
    def __init__(self, bgp_agent, events):
        self.agent = bgp_agent
        table = 'Load_Balancer'
        super(OVNLBMemberEvent, self).__init__(
            events, table, None)
        self.event_name = self.__class__.__name__


class LSPChassisEvent(row_event.RowEvent):
    def __init__(self, bgp_agent, events):
        self.agent = bgp_agent
        table = 'Logical_Switch_Port'
        super(LSPChassisEvent, self).__init__(
            events, table, None)
        self.event_name = self.__class__.__name__

    def _check_ip_associated(self, mac):
        return len(mac.strip().split(' ')) > 1
