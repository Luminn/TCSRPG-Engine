import pygame
from GraphicsEngine.TileMap import TileSize, GetDisplayedCoords

_graphicsStack = []

_graphicsDict = {}

ALPHA = [255, 120, 80, 40, 0]

def Draw(list_of_squares, color, alpha=1):
    l = []
    r,g,b = color[:3]
    a = ALPHA[alpha]
    l.append((r,g,b,a))
    l.extend(list_of_squares)
    _graphicsStack.append(l)


def Clean():
    global _graphicsStack, _graphicsStack1
    _graphicsStack = []


def RangeDisplayLoop(screen):
    seen = set()
    for i in reversed(_graphicsStack):
        color = i[0]
        for c in i[1:]:
            if c in seen:
                continue
            seen.add(c)
            s = pygame.Surface((TileSize, TileSize), pygame.SRCALPHA)
            s.fill(color)
            screen.blit(s, GetDisplayedCoords(c))

    for key in _graphicsDict:
        i = _graphicsDict[key]
        color = i[0]
        for c in i[1:]:
            if c in seen:
                continue
            seen.add(c)
            s = pygame.Surface((TileSize, TileSize), pygame.SRCALPHA)
            s.fill(color)
            screen.blit(s, GetDisplayedCoords(c))

def DrawKey(key, list_of_squares, color, alpha=1):
    l = []
    r,g,b = color[:3]
    a = ALPHA[alpha]
    l.append((r,g,b,a))
    l.extend(list_of_squares)
    _graphicsDict[key] = l


def RemoveKey(key):
    _graphicsDict.pop(key)


def HasKey(key):
    return key in _graphicsDict


def CleanKeys():
    global _graphicsDict
    _graphicsDict = {}