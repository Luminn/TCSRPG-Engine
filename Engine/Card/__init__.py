
from Engine.Interfaces import StatGetter, EventListener
from typing import Tuple
from Definitions.Card import *

MainCardCollection = []

# we defined a bunch of functions for engine use
class Card(EventListener):

    def __init__(self, name, description, vigor_cost, sprite, card_class):
        MainCardCollection.append(self)
        self.id = len(MainCardCollection) - 1
        self.name = name
        self.description = description
        self.cost = vigor_cost
        self.card_class = card_class
        self.sprite = sprite

    def GetCost(self, owner)->int:
        return self.cost

    def GetRange(self, owner)->Tuple[int, int]:
        return 0, 0 # default self cast buff

    # If true show up on attack map
    def IsAttack(self, owner)->bool:
        return False

    # If true show up on range map
    def IsMovement(self, owner)->bool:
        return False
        # If true show up on range map

    # Test other custom stuff, default false
    def IsCondition(self, owner, qualifier) -> bool:
        return False

    # if return false, will not appear in draw pile, eg: weapon attack without a weapon
    def CanUse(self, owner)->bool:
        return True

    # usable but not optimal, could be removed depend on the rules
    def IsUnoptimized(self, owner) -> bool:
        return True

    # if return false, card cannot be played when in hand
    # should check acceptable targets first
    def CanPlay(self, owner)->bool:
        return True

    # if condition is met, force unit to draw this card
    # only activates on drawing phase
    def IsTutored(self, owner)->bool:
        return False

    # if condition is met, unit does not shuffle this card into the discard pile
    def IsRetained(self, owner)->bool:
        return False

    # what happens if drawn, return a buff or None,
    # will be tracked by the deck and end with the card being discarded
    # and can do other stuff with this
    def OnDraw(self, owner)->Buff:
        return None

    # what happens if discarded
    def OnDiscard(self, owner):
        pass

    # after hover, call some event script
    # usually draw the attack range
    def OnHover(self, owner):
        pass

    # after hover end, call some event script
    # usually remove the attack range drawn
    def OnHoverEnd(self, owner):
        pass

    # after select, call some event script
    # returns target or none, if no target needed, return owner
    # will not be called by ai
    def OnSelect(self, owner):
        pass

    # perform action, after card is confirmed to be played
    # don't launch any ui prompts here
    # must be safe for ai to use
    def OnPlay(self, owner, target):
        pass

    # called when ai is selected to play this
    # return (target, priority) priority in [0,100)
    # return (None, 0) if ai cannot play this
    def OnAI(self, owner):
        return None, 0


def GetCard(id:int)->Card:
    return MainCardCollection[id]