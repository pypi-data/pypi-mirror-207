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

from typing import Union, List, Tuple, Optional, Dict
from .object import Object


class Node(object):
    PORT = 3610

    __address: Optional[Tuple[str, int]]
    __objects: Dict[int, Object]

    def __init__(self, addr: Optional[Tuple[str, int]] = None):
        self.__address = ()
        self.__objects = {}
        self.set_address(addr)

    def set_address(self, addr: Tuple[str, int]) -> bool:
        if not isinstance(addr, tuple) or len(addr) != 2:
            return False
        self.__address = addr
        return True

    @property
    def address(self) -> Optional[Tuple[str, int]]:
        return self.__address

    @property
    def ip(self) -> str:
        if len(self.__address) != 2:
            return ""
        return self.__address[0]

    @property
    def port(self) -> int:
        if len(self.__address) != 2:
            return 0
        return Node.PORT

    def add_object(self, obj: Object) -> bool:
        if not isinstance(obj, Object):
            return False
        self.__objects[obj.code] = obj
        obj.node = self
        return True

    @property
    def objects(self) -> List[Object]:
        objs = []
        for obj in self.__objects.values():
            objs.append(obj)
        return objs

    def has_object(self, code: int) -> bool:
        return code in self.__objects.keys()

    def get_object(self, code: Union[int, Tuple[int, int, int]]) -> Optional[Object]:
        """ Returns the object specified the code.

        Args:
            code (Union[str, Tuple[int, int, int]]): A object code.

        Returns:
            Optional[Object]: Returns the object when the node has the object specified by the code, otherwise None.
        """
        obj = Object(code)
        try:
            return self.__objects[obj.code]
        except KeyError:
            return None
