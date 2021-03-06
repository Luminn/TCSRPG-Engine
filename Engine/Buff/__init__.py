from __future__ import annotations
from typing import List, Union, BinaryIO

from Engine.Interfaces import StatGetter, IBuff
from Engine.Timer import Timer
from Engine.Save import SaveShort, SaveInt, SaveChunk

_buff_collection:List[BuffDefinition] = []

# The saved instance of a buff
class Buff(IBuff, SaveChunk):

    def __init__(self, uid:int=0, timer_type:int=0, timer:int=0, counter:int=0, owner:IBuff=None):
        self.uid = uid
        self.timer_type = timer_type
        self.timer = timer
        self.counter = counter
        self.owner = owner
        self.buff_data = _buff_collection[uid]

    def GetData(self):
        return self.timer_type, self.timer, self.counter, self.owner

    def GetStat(self, statName):
        result = self.buff_data.GetStat(statName, self.GetData())
        if result is None:  # if not implemented
            return StatGetter.Default(statName)
        return result

    def GetChild(self):
        return [Timer(self.timer_type, self.timer)]

    def Listen(self, event, data):
        n = self.buff_data.Listen(event, data, self.GetData())
        if n is not None:
            self.timer, self.counter = n

    def Timeout(self):
        return self.timer_type != 0 and self.timer <= 0

    def SaveDataLength(self):
        return len(self.SavedArray())

    def SavedArray(self):
        return self.uid, self.timer_type, self.timer, self.counter

    def ReadSave(self, data):
        self.uid, self.timer_type, self.timer, self.counter = data

    def Read(self, stream:BinaryIO):
        self.uid = SaveInt().Read(stream)
        self.counter = SaveInt().Read(stream) # for rng seed
        self.timer_type = SaveShort().Read(stream)
        self.timer = SaveShort().Read(stream)
        self.buff_data = _buff_collection[self.uid]
        return self

    def Write(self, stream:BinaryIO):
        SaveInt(self.uid).Write(stream)
        SaveInt(self.counter).Write(stream)
        SaveShort(self.timer_type).Write(stream)
        SaveShort(self.timer).Write(stream)


# the core stuff of a buff
class BuffDefinition:


    def __init__(self):
        _buff_collection.append(self)
        self.uid = len(_buff_collection) - 1

    # can return new timer, new counter
    # buff_data is timer_uid, timer, counter, owner
    def Listen(self, event, data, buffData)->Union[(int,int),None]:
        pass

    # buff_data is timer_uid, timer, counter, owner
    def GetStat(self, statName, buffData)->Union[int,bool]:
        pass

