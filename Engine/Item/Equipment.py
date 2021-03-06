
from Engine.Buff import BuffList
from Engine.Item import GameItem

class Equipment(BuffList, GameItem):

    def __init__(self, name, description, sprite, slots):
        GameItem.__init__(self, name, description, sprite)
        self.equipment_slots = slots

    def Equippable(self, user, slot):
        return slot == self.equipment_slots or slot in self.equipment_slots
