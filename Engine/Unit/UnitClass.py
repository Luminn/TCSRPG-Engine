
from Definitions.Unit import MALE, FEMALE
from Definitions.Tiles import StandardMovement
from Engine.Unit import Unit

# just a definition, also finds class sprites, curators does actual heavy lifting
_classes = []
class UnitClass:

    def __init__(self, name, description, male_sprites=(), female_sprites=(), movement_type=StandardMovement):
        self.name = name
        self.description = description
        self.male_sprites = male_sprites
        self.female_sprites = female_sprites
        self.terrain_type = movement_type
        self.uid = len(_classes)
        _classes.append(self)

    def GetSprite(self, index, gender):
        if gender == FEMALE:
            return self.female_sprites[index]
        else:
            return self.male_sprites[index]

def GetClass(index:int)->UnitClass:
    return _classes[index]

def GetUnitClass(unit:Unit)->UnitClass:
    return GetClass(unit.info.class_id)

DummyClass = UnitClass("Dummy", "Dummy")