from __future__ import annotations
from typing import Union, List


class StatGetter:

    MultiplierPrefix = "m_"
    BooleanPrefix = "is_"

    @staticmethod
    def Default(statName:str)->Union[int,bool]:
        if statName.startswith(StatGetter.MultiplierPrefix):
            return 1
        if statName.startswith(StatGetter.BooleanPrefix):
            return False
        return 0

    def GetStat(self, statName:str)->Union[int,bool]:
        pass

class StatSetter:

    def SetStat(self, statName:str, value)->Union[int,bool]:
        pass


class SaveDict:

    def Get(self, StatName):
        pass

    def Set(self, statName, value):
        pass


class EventListener:

    def _listen(self, event:str, data:dict):
        for i in self.GetChild():
            i._listen(event, data)
        self.Listen(event, data)

    def GetChild(self)->List[EventListener]:
        return []

    def Listen(self, event:str, data:dict):
        pass


class IBuff(StatGetter, EventListener):
    pass