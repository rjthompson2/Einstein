from typing import Any
class ArguementMap():
    def __init__(self):
        self.map = {}

    def add(self, values:list) -> None:
        last_flag = None
        for value in values:
            if self.type_flag(value):
                self.map[value] = ''
                last_flag = value
            elif last_flag:
                self.map[last_flag] += str(value)
    
    def get(self, flag:str) -> Any:
        if flag in self.map:
            return self.map[flag]
        return None

    def get_map(self) -> dict:
        return self.map

    def type_flag(self, value:str) -> bool:
        return value.startswith('-')

    def __repr__(self) -> str:
        return str(self.map)


class ArguementMapTimer(ArguementMap):
    def type_flag(self, value:str) -> bool:
        flags = ['for', 'at', 'in', 'on']
        return value in flags