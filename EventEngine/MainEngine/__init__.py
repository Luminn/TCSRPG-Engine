from Engine.Unit import Unit, DummyUnit
from Engine.Unit.Allegiance import IsPlayer
from EventEngine.Stage.AdvancedCalculators import AdvancedAttackRange
from Engine.Unit.UnitClass import GetUnitClass
from EventEngine.MainEngine.Animations import PlayMove, PlayAttack
from EventEngine.MainEngine.Prompts import RangeDisplayPrompt, RangeDisplayPrompt2, EnemyRangeAdd, EndRangePrompt
import EventEngine.Variables as Vars
from GraphicsEngine.TileMap import ColoredOverlay
from Definitions.Allegiance import MoveThrough

# vigor cost of selected card
def _vigorCost():
    return 1

def OnSelectUnit(unit:Unit):
    if IsPlayer(unit) and not Vars.TurnUserLockedIn:
        Vars.CurrentUnit = unit
    ColoredOverlay.Clean()
    m1 = m2 = unit.GetStat("movement")
    r = AdvancedAttackRange(unit)
    if Vars.PromptUnit != unit:
        if unit.coords in Vars.PromptTargets:
            if Vars.PromptType == Vars.PromptMove:
                pass
            elif Vars.PromptType == Vars.PromptAttack:
                PlayAttack(Vars.CurrentUnit, unit)
        else:
            RangeDisplayPrompt(unit.coords, m1, r, GetUnitClass(unit).terrain_type, MoveThrough(unit.allegiance))
            Vars.RangePromptOn, Vars.AdvancedRangePromptOn = True, False
            Vars.PromptUnit = unit
    elif Vars.AdvancedRangePromptOn or (Vars.RangePromptOn and m1 == m2):
        Vars.RangePromptOn, Vars.AdvancedRangePromptOn = False, False
        Vars.PromptUnit = DummyUnit
    elif Vars.RangePromptOn:
        RangeDisplayPrompt2(unit.coords, m2, r, GetUnitClass(unit).terrain_type, MoveThrough(unit.allegiance))
        RangeDisplayPrompt(unit.coords, m1, r, GetUnitClass(unit).terrain_type, MoveThrough(unit.allegiance))
        Vars.RangePromptOn, Vars.AdvancedRangePromptOn = False, True
    else:
        Vars.RangePromptOn, Vars.AdvancedRangePromptOn = False, False
        Vars.PromptUnit = DummyUnit

def OnSecondarySelectUnit(unit:Unit):
    c = unit.coords
    m2 = unit.GetStat("movement")
    r = AdvancedAttackRange(unit)
    if ColoredOverlay.HasKey(c):
        ColoredOverlay.RemoveKey(c)
    else:
        EnemyRangeAdd(c, m2, r, GetUnitClass(unit).terrain_type, MoveThrough(unit.allegiance))


def OnSelectTile(coords):
    if coords in Vars.PromptTargets and Vars.PromptType == Vars.PromptMove:
        PlayMove(Vars.CurrentUnit, coords)
    else:
        EndRangePrompt()

def OnSecondarySelectTile(coords:tuple):
    if coords in Vars.PromptTargets and Vars.PromptType == Vars.PromptMove:
        PlayMove(Vars.CurrentUnit, coords)
    elif coords in Vars.PromptTargets and Vars.PromptType == Vars.PromptDisplay:
        pass #TODO: implement movement queue

def OnCardSelect(unit:Unit, card_slot):
    SelectedCard = card_slot
    # TODO: anim


def OnCardPlay(unit:Unit, card_slot):
    pass


def OnSkillSelect(unit:Unit, skill_slot):
    pass


def OnSkillPlay(unit:Unit, skill_slot):
    pass



