from Definitions import Colors
from Definitions.Allegiance import MoveThrough
import EventEngine.Variables as Vars
from EventEngine.Stage import MainStage
from GraphicsEngine.TileMap import ColoredOverlay


def MovePrompt(src, move, terrain_cost):
    display, real = MainStage.MovementMap(src.coords, move, terrain_cost, MoveThrough(src.allegiance))
    Vars.PromptTargets = real
    ColoredOverlay.Draw(display, Colors.BLUE)


def WarpPrompt(src, range, terrain_cost):
    pass


def AttackPrompt(src, range, allegiance):
    display, real = MainStage.AttackMap(src.coords, range, allegiance)
    Vars.PromptTargets = real
    ColoredOverlay.Draw(display, Colors.RED)


# show max movement with 1 vigor + attack range
def RangeDisplayPrompt(src, move, range, terrain_cost, allegiance):
    range_map, _ = MainStage.MovementMap(src, move, terrain_cost, allegiance)
    attack_map, _ = MainStage.AttackMapFromMovementMap(range_map, range, allegiance)
    ColoredOverlay.Draw(attack_map, Colors.RED)
    ColoredOverlay.Draw(range_map, Colors.BLUE)


# show full movement + attack range
def RangeDisplayPrompt2(src, move, range, terrain_cost, allegiance):
    range_map, _ = MainStage.MovementMap(src, move, terrain_cost, allegiance)
    attack_map, _ = MainStage.AttackMapFromMovementMap(range_map, range, allegiance)
    ColoredOverlay.Draw(attack_map, Colors.LIGHTCORAL)
    ColoredOverlay.Draw(range_map, Colors.LIGHTBLUE)


def EnemyRangeAdd(src, move, range, terrain_cost, allegiance):
    range_map, _ = MainStage.MovementMap(src, move, terrain_cost, allegiance)
    attack_map, _ = MainStage.AttackMapFromMovementMap(range_map, range, allegiance)
    ColoredOverlay.DrawKey(src, attack_map, Colors.ORANGE)


def EndRangePrompt():
    Vars.RangePromptOn = False
    Vars.AdvancedRangePromptOn = False
    Vars.PromptType = Vars.PromptNo
    Vars.PromptTargets = []
    ColoredOverlay.Clean()