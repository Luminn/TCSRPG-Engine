
from Engine.Buff.BuffList import BuffList

_items = []

class GameItem(BuffList):


    def __init__(self, name, description, sprite):
        self.name = name
        self.description = description
        self.sprite = sprite
        _items.append(self)
        self.id = len(_items) - 1

    def Equippable(self, user, slot):
        return False

    def Usable(self, user):
        return False

def GetItem(uid):
    return _items[uid]


DummyItem = GameItem("Dummy", "Dummy", None)