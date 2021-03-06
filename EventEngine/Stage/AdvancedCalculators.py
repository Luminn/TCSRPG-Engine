from Engine.Unit import Unit
from Engine.Card import GetCard
from Engine.Card.Templates import MovementCard
import Definitions.Unit as Stats
from Definitions.Unit import VIGOR
from Definitions.Allegiance import MoveThrough
from Engine.Unit.UnitClass import GetUnitClass

from EventEngine.Stage import MainStage

#returns the mov by a single card/skill that returns a non zero movement queue priority
def MaxSuggestedMove(unit:Unit):
    result = set()
    v = unit.GetStat(VIGOR)
    for i in unit.deck.Hand + unit.deck.TempHand:
        c = GetCard(i)
        if isinstance(c, MovementCard) and c.MovementQueue(unit) != 0 and c.GetCost(unit) <= v:
            m = c.GetMovement(unit)
            if c.IsWarp(unit):
                r = MainStage.WarpMap(unit.coords, m, GetUnitClass(unit).terrain_type, MoveThrough(unit.allegiance))
            else:
                r = MainStage.MovementMap(unit.coords, m, GetUnitClass(unit).terrain_type, MoveThrough(unit.allegiance))
            result = result.union(r)
    return result


# returns the max possible move using all of the unit's energy
def MaxMove(unit:Unit):
    v = unit.GetStat(VIGOR)
    result = []
    for i in range(v):
        pass




def AdvancedAttackRange(unit:Unit, vigor=-1):
    return 1
    #todo: maximum attack range