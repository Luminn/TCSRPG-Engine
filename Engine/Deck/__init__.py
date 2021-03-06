from typing import BinaryIO
from Engine.Rng import MainRNG
from Engine.Save import SaveChunk
from Engine.Save.Arrays import SaveIntArray, SaveShortArray
from Engine.Buff.BuffList import BuffArray
from Engine.Card import GetCard
from enum import Enum

MAX_HAND_SIZE = 12

class HandDisplay(Enum):
    regular = 0
    temporary = 1


def Shuffle(deck, rng):
    for i in reversed(range(1, len(deck))):
        j = MainRNG.RandInt(rng, i + 1)
        deck[i], deck[j] = deck[j], deck[i]


class Deck(SaveChunk):

    def __init__(self, owner):
        self.Owner = owner
        self.Deck = []
        self.Hand = []
        self.DrawPile = []
        self.DiscardPile = []

        self.InHandBuffs = []

        self.CooldownPile = []
        self.CooldownCount = []

    def Read(self, stream:BinaryIO):
        self.Deck = SaveIntArray().Read(stream)
        self.Hand = SaveIntArray().Read(stream)
        self.DrawPile = SaveIntArray().Read(stream)
        self.DiscardPile = SaveIntArray().Read(stream)
        self.CooldownPile = SaveIntArray().Read(stream)
        self.CooldownCount = SaveShortArray().Read(stream)
        self.InHandBuffs = BuffArray().Read(stream)


    def Write(self, stream:BinaryIO):
        SaveIntArray(self.Deck).Write(stream)
        SaveIntArray(self.Hand).Write(stream)
        SaveIntArray(self.HandOrder).Write(stream)
        SaveIntArray(self.DrawPile).Write(stream)
        SaveIntArray(self.DiscardPile).Write(stream)
        SaveIntArray(self.CooldownPile).Write(stream)
        SaveShortArray(self.CooldownCount).Write(stream)
        BuffArray(self.InHandBuffs).Write(stream)

    def ResetDeck(self):
        self.Hand = []
        self.InHandBuffs = []
        self.DrawPile = []
        self.DiscardPile = []
        self.CooldownPile = []
        self.CooldownCount = []

    def InitializeDrawPile(self, rng=0):
        self.ResetDeck()
        deck = self.Deck
        Shuffle(deck, rng)
        self.DrawPile = deck


    def ShuffleDrawPile(self, rng=0):
        deck = self.DiscardPile + self.DrawPile
        Shuffle(deck, rng)
        self.DrawPile = deck
        self.DiscardPile = []

    def DrawHand(self, hand_size):
        if hand_size + len(self.Hand) > MAX_HAND_SIZE:  # safety first
            hand_size = MAX_HAND_SIZE - len(self.Hand)
        new_hand = []
        new_draw_pile = []
        for i in self.DrawPile: # search for forced draws
            if hand_size < len(new_hand) and GetCard(i).IsTutored(self.Owner):
                new_hand.append(i)
            else:
                new_draw_pile.append(i)
        self.DrawPile = new_draw_pile
        if hand_size - len(new_hand) <= len(self.DrawPile):
            new_hand += self.DrawPile[:hand_size - len(new_hand)]
            self.DrawPile = self.DrawPile[hand_size:]
        else:
            new_hand += self.DrawPile
            self.ShuffleDrawPile()
            if len(new_hand) + len(self.DrawPile) >= hand_size:
                new_hand += self.DrawPile[:hand_size - len(new_hand)]
                self.DrawPile = self.DrawPile[hand_size:]
            else:
                new_hand += self.DrawPile
                self.DrawPile = []
        self.Hand.extend(new_hand) # keep retained hand here
        self.InHandBuffs.extend([i.InHandBuff(self.Owner) for i in new_hand])


    def DrawCardByNumber(self, number):
        new_hand = []
        if number <= len(self.DrawPile):
            new_hand += self.DrawPile[:number - len(new_hand)]
            self.DrawPile = self.DrawPile[number:]
        else:
            new_hand += self.DrawPile
            self.ShuffleDrawPile()
            if len(new_hand) + len(self.DrawPile) >= number:
                new_hand += self.DrawPile[:number - len(new_hand)]
                self.DrawPile = self.DrawPile[number:]
            else:
                new_hand += self.DrawPile
                self.DrawPile = []
        self.Hand.extend(new_hand) # keep retained hand here

    def AddCardToHand(self, card, where=-1):
        if where == -1:
            where = len(self.Hand)
        self.DrawAddCard(card, where)
        self.InHandBuffs.insert(where, card.InHandBuff(self.Owner))


    def DiscardHand(self):
        discarded = []
        retained = []
        for i in self.Hand:
            if GetCard(i).IsRetained(self.Owner):
                retained.append(i)
            else:
                discarded.append(i)
        self.DiscardPile.extend(discarded)
        self.InHandBuffs= []
        self.Hand = retained

    def DrawAddCard(self, card, where=-1):
        pass #todo: talk to event engine, low prio

    def DrawFromDrawPile(self, cards):
        pass #todo: talk to event engine, low prio

    # maybe we don't need this lmao
    def DrawDiscard(self):
        pass #todo: talk to event engine, low prio