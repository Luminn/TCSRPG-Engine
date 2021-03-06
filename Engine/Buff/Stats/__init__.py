from Engine.Buff import BuffDefinition
from Engine.Interfaces import StatGetter
from Definitions import Unit as Stats

class Stat(BuffDefinition):
    def __init__(self, statName):
        BuffDefinition.__init__(self)
        self.statName = statName

    def GetStat(self, statName, buffData):
        if statName == self.statName:
            _, _, counter, _ = buffData
            return counter
        else:
            return StatGetter.Default(statName)

X = Stat(Stats.X).uid
Y = Stat(Stats.Y).uid
MaxHP = Stat(Stats.MAX_HP).uid
HP = Stat(Stats.HP).uid
HPGrowth = Stat(Stats.HP_GROWTH).uid
Strength = Stat(Stats.STRENGTH).uid
StrengthGrowth = Stat(Stats.STRENGTH_GROWTH).uid
Magic = Stat(Stats.MAGIC).uid
MagicGrowth = Stat(Stats.MAGIC_GROWTH).uid
Defense = Stat(Stats.DEFENSE).uid
DefenseGrowth = Stat(Stats.DEFENSE_GROWTH).uid
Resistance = Stat(Stats.RESISTANCE).uid
ResistanceGrowth = Stat(Stats.RESISTANCE_GROWTH).uid
Speed = Stat(Stats.SPEED).uid
SpeedGrowth = Stat(Stats.SPEED_GROWTH).uid
Movement = Stat(Stats.MOVEMENT).uid
MovementGrowth = Stat(Stats.MOVEMENT_GROWTH).uid
Draw = Stat(Stats.DRAW).uid
DrawGrowth = Stat(Stats.DRAW_GROWTH).uid
MaxVigor = Stat(Stats.MAX_VIGOR).uid
Vigor = Stat(Stats.VIGOR).uid


