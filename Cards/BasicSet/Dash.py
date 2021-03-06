from Engine.Card.Templates import MovementCard
from Definitions.Unit import MOVEMENT

class BSC_Dash(MovementCard):

    def GetCost(self, owner):
        return 1

    def GetMovement(self, owner):
        return owner.GetStat(MOVEMENT)