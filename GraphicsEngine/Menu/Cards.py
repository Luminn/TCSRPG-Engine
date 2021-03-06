
from pygame import freetype
from Engine.Card import GetCard
from GraphicsEngine.Sprites import GetSprite
from GraphicsEngine.ScreenSprite import ScreenSprite
from GraphicsEngine.Cards.CardBack import GetCardBack
from TextEngine import DescriptionText
import EventEngine.Variables as Vars

freetype.init()
NameFont = freetype.SysFont("Helvetica", 20)
On = True

class CardSprite(ScreenSprite):

    def __init__(self, card, owner, coords, fx):
        card = GetCard(card)
        self.fx = fx
        name = card.name
        description = card.description
        cost = card.GetCost(owner)
        description_object = DescriptionText(description)
        sprite = GetSprite(card.sprite)
        card_back = GetCardBack(card.card_class)
        ScreenSprite.__init__(self, card_back, coords, scale=1)
        name_surface = NameFont.render(name, False, (0, 0, 0))
        self.blit(name_surface, (0, 0))


_cards = []


def GetStaticCoords(index):
    return 600, 100 * index

# update hand, run this after animation stuff
def UpdateHand():
    global _cards
    if Vars.CurrentUnit is None:
        _cards = []
    hand = Vars.CurrentUnit.deck.HandOrder
    display_mode = Vars.CurrentUnit.deck.HandDisplay

    for i,v in enumerate(hand):
        _cards.append(CardSprite(v, Vars.CurrentUnit, GetStaticCoords(i), display_mode))


# draw a card
def DrawCard():
    pass

def HandLoop(screen, dt):
    if not On:
        pass
    for i in _cards:
        i.Update(dt)
        if i.visible:
            c = i.GetCoords()
            screen.blit(i, c)




