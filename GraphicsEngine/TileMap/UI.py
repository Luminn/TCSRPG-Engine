

import pygame
from Definitions.Graphics import TileSize, OverlayAlpha
import GraphicsEngine.TileMap as TileMap

DrawTileMap = {}

def MapUiLoop(screen):
    for coords in DrawTileMap:
        color = DrawTileMap[coords]
        x, y = TileMap.GetDisplayedCoords(coords)
        r, g, b, _ = color
        s = pygame.Surface((TileSize, TileSize))
        s.set_alpha(OverlayAlpha)
        s.fill(color)
        screen.blit(s, (x,y))

def Draw(color, coords, overwrite=True):
    for c in coords:
        if overwrite or c not in DrawTileMap:
            DrawTileMap[c] = color

def Clean():
    global DrawTileMap
    DrawTileMap = {}

