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

import socket
import threading
from typing import Any, Optional, List

from ..protocol.message import Message
from ..protocol.observer import Observer
from ..protocol.subject import Subject
from ..log.logger import error, debug


class Server(threading.Thread):
    PORT = 3610

    sock: Optional[socket.socket]
    ifaddr: str
    port: int
    __msg_subject: Subject

    def __init__(self):
        super().__init__()
        self.sock = None
        self.ifaddr = ""
        self.port = Server.PORT
        self.__msg_subject = Subject()

    def __del__(self):
        self.stop()

    def create_udp_socket(self) -> socket.socket:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        return sock

    def bind(self, ifaddr: str) -> bool:
        self.ifaddr = ifaddr
        return True

    def run(self):
        while True:
            try:
                if self.sock is None:
                    break

                recv_msg_bytes, recv_from = self.sock.recvfrom(1024)

                recv_msg_prefix = '%s:%s <- %s:%s' % (self.ifaddr.ljust(15), str(self.port).ljust(5), recv_from[0].ljust(15), str(recv_from[1]).ljust(5))

                msg = Message()
                if not msg.parse_bytes(recv_msg_bytes):
                    error('%s %s' % (recv_msg_prefix, recv_msg_bytes.hex()))
                    continue

                msg.from_addr = recv_from
                debug('%s %s' % (recv_msg_prefix, msg.to_string()))
                self.notify(msg)
            except:
                break

    def add_observer(self, observer) -> bool:
        """ Adds a message observer to the subject.

        Args:
            observer Observer: A message observer.

        Returns:
            bool: Returns True when the specified observer is added, Otherwise False.

        """
        return self.__msg_subject.add_observer(observer)

    def notify(self, msg: Message):
        """Notifies the specified message to the added observers.

        Args:
            msg (Message): A notify message 
        """
        self.__msg_subject.notify(msg)

    def start(self) -> Any:
        if self.sock is None:
            return False
        super(Server, self).start()
        return True

    def stop(self) -> Any:
        if self.sock is None:
            return False
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
        except:
            pass
        self.sock.close()
        self.sock = None
        self.join()
        return True
