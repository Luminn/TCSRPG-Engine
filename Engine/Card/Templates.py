
from Engine.Card import Card
from Engine.Unit.UnitClass import GetUnitClass
#from EventEngine.MainEngine import PlayMove
from EventEngine.MainEngine.Prompts import AttackPrompt, MovePrompt

import Definitions.Unit as Stats

class AttackCard(Card):

    def IsAttack(self, owner):
        return True

    def OnSelect(self, owner):
        pass


class MovementCard(Card):

    def IsMovement(self, owner):
        return True

    # ignores terrain
    def IsWarp(self, owner):
        return False

    def GetMovement(self, owner):
        return owner.GetStat(Stats.MOVEMENT)

    # move(1 energy for MOV move) returns 4, return less if more efficient, 0 if not recommended in the queue
    def MovementQueue(self, owner):
        return self.GetMovement(owner) * 2 / self.GetCost(owner) + 1

    def OnSelect(self, owner):
        MovePrompt(owner, self.GetMovement(owner), GetUnitClass(owner).terrain_type)

    def OnPlay(self, owner, target):
        pass
        #PlayMove(owner, target)

