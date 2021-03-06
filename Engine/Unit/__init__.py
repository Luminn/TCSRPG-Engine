from Engine.Buff import Buff
from Engine.Buff.BuffList import BuffList, BuffArray
from Engine.Save import SaveChunk, SaveInt, SaveString, SaveShort, SaveByte
from Engine.Save.Arrays import SaveShortArray, SaveIntArray
from Engine.Deck import Deck
from Engine.Item import GetItem
from typing import BinaryIO

# not saved, players and stage stores and reads units
_global_unit_dict = {}
_ptr = 1

# we define things that're not numerical stats here
class UnitInfo(SaveChunk):

    def __init__(self, name="", class_id=0, gender=0, sprite_index=0, portrait=0):
        self.name = name
        self.class_id = class_id
        self.gender = gender
        self.sprite_index = sprite_index
        self.portrait = portrait

    def Read(self, stream:BinaryIO):
        self.name = SaveString().Read(stream)
        self.class_id = SaveShort().Read(stream)
        self.gender = SaveByte().Read(stream)
        self.sprite_index = SaveByte().Read(stream)
        self.portrait = SaveShort().Read(stream)

    def Write(self, stream:BinaryIO):
        SaveString(self.name).Write(stream)
        SaveShort(self.class_id).Write(stream)
        SaveByte(self.gender).Write(stream)
        SaveByte(self.sprite_index).Write(stream)
        SaveShort(self.portrait).Write(stream)

# we keep stats in buff list and animation stuff out of it?
class Unit(BuffList, SaveChunk):

    @staticmethod
    def GetNextID():
        global _ptr
        while True:
            if _ptr not in _global_unit_dict:
                return _ptr
            _ptr += 1

    def __init__(self, id=0):
        self.id = id
        self.coords = (0,0)
        self.allegiance = 0
        self.info = UnitInfo()
        self.stats = BuffArray()
        self.buffs = BuffArray()
        self.equipments = SaveIntArray([0, 0, 0])
        self.deck = Deck(self)
        self.map_unit = None
        if id != 0:
            self._storeUnit()

    def GetBuffs(self):
        return self.stats + self.buffs + [j for i in [GetItem(j).GetBuffs() for j in self.equipments] for j in i]

    def Read(self, stream):
        self.id = SaveInt().Read(stream)
        self.coords = SaveShort().Read(stream), SaveShort().Read(stream)
        self.allegiance = SaveByte().Read(stream)
        self.info.Read(stream)
        self.stats.Read(stream)
        self.buffs.Read(stream)
        self.equipments.Read(stream)
        self.deck.Read(stream)
        self._storeUnit()

    def Write(self, stream):
        SaveInt(self.id).Write(stream)
        SaveShort(self.coords[0]).Write(stream)
        SaveShort(self.coords[1]).Write(stream)
        SaveByte(self.allegiance).Write(stream)
        self.info.Write(stream)
        self.stats.Write(stream)
        self.buffs.Write(stream)
        self.equipments.Write(stream)
        self.deck.Write(stream)

    def SetStat(self, stat:int, value:int):
        if stat in self.stats:
            self.stats.SetCounter(stat, value)
        else:
            self.stats.append(Buff(stat,0,0,value))

    def _storeUnit(self):
        global _ptr
        _global_unit_dict[id] = self
        if _ptr == self.id - 1 or _ptr == id:
            _ptr = self.id + 1


DummyUnit = Unit()