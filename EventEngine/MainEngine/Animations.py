
from Engine.Unit import Unit


def PlayMove(unit:Unit, to):
    unit.map_unit.AnimatedMove(to)


def PlayAttack(unit:Unit, target):
    unit.map_unit.AnimatedAttack(target, [])
