# Copyright (C) 2021 Satoshi Konno. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc
from .message import Message


class Observer(metaclass=abc.ABCMeta):
    """Observer is an abstract observer class to listen to request messages to a device.
    """

    @abc.abstractmethod
    def message_received(self, msg: Message):
        """ Listens a request message from other nodes

        Args:
            msg (Message): A request message from other nodes
        """
        pass
