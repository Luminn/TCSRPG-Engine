from typing import List

from typing import BinaryIO
from Engine.Buff import Buff, BuffDefinition
from Engine.Interfaces import IBuff, StatGetter
from Engine.Save import SaveInt, SaveChunk
from Engine.Save.Arrays import SaveShortArray


# List of IBuffs, also an IBuff so can contain itself
class BuffList(IBuff):

    def GetBuffs(self)->List[IBuff]:
        return []

    def GetStat(self, statName:str):
        if statName.startswith(StatGetter.BooleanPrefix):
            for i in self.GetBuffs():
                if i.GetStat(statName):
                    return True
            return False
        elif statName.startswith(StatGetter.MultiplierPrefix):
            n = 1
            for i in self.GetBuffs():
                x = i.GetStat(statName)
                if x is not None:
                    n *= x
            return n
        else:
            n = 0
            for i in self.GetBuffs():
                x = i.GetStat(statName)
                if x is not None:
                    n += x
            return n

    def GetChild(self):
        return self.GetBuffs()


# Saved BuffList, list of buffs only
class BuffArray(BuffList, list, SaveChunk):

    def __init__(self, content = ()):
        list.__init__(self, content)

    def __contains__(self, item):
        for i in self:
            if i == item:
                return True
            elif i.uid == item:
                return True
            elif isinstance(item, BuffDefinition) and item.uid == i.uid:
                return True
        return False

    def GetBuffs(self)->List[Buff]:
        return self

    def Read(self, stream:BinaryIO):
        self.clear()
        n = SaveInt().Read(stream)
        for i in range(n):
            self.append(Buff().Read(stream))

    def Write(self, stream:BinaryIO):
        SaveInt(len(self)).Write(stream)
        for i in self:
            i.Write(stream)

    def FindBuff(self, item):
        for i in self:
            if i == item:
                return i
            elif i.uid == item:
                return i
            elif isinstance(item, BuffDefinition) and item.uid == i.uid:
                return i
        return None

    def SetCounter(self, item, value):
        for i in self:
            if i.uid == item:
                i.counter = value
                return
            elif isinstance(item, BuffDefinition) and item.uid == i.uid:
                i.counter = value
                return
        return None