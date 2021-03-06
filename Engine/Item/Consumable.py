
from Engine.Buff import BuffList
from Engine.Item import GameItem

class Equipment(BuffList, GameItem):

    def __init__(self, name, description, sprite, slot):
        GameItem.__init__(self, name, description, sprite)
        self.equipment_slot = slot

