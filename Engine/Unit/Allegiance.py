
from Engine.Unit import Unit
import Definitions.Allegiance as Al

def IsPlayer(unit:Unit):
    return unit.allegiance == Al.Player

def IsEnemy(unit:Unit):
    return unit.allegiance in Al.PlayerTarget

def IsNPC(unit:Unit):
    return unit.allegiance in Al.Ally, Al.Neutral

