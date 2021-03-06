import pygame
import GraphicsEngine.TileMap as TileMap
from GraphicsEngine.GameSprite import GameSprite
from enum import Enum

MapCursorMargin = (3,3)
MapCursorCoordinates = (0, 0)
CursorCoordinates = 0
CursorMax = 1

CursorImage = pygame.image.load("image/mapsprite/FECursor.png")

MapCursor = GameSprite(CursorImage, (1,1), (0,0), (2,2))
TileMap.TiledSprites.add(MapCursor)

KeyCooldown = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_UP: False, pygame.K_DOWN: False}
Cooldown = 80
Counter = 0

FirstKey = True
RollBack = (-1, -1)

def KeyDownHandler(key, delta):
    global MapCursorCoordinates, Counter, FirstKey, RollBack
    if Counter > Cooldown:
        Counter = 0
        KeyCooldown[pygame.K_LEFT] = KeyCooldown[pygame.K_RIGHT] = KeyCooldown[pygame.K_DOWN] \
            = KeyCooldown[pygame.K_UP] = False
    Counter += delta
    if Counter > Cooldown/2:
        return
    x,y = MapCursorCoordinates
    if key in KeyCooldown and not KeyCooldown[key]:
        KeyCooldown[key] = True
        if key == pygame.K_LEFT:
            x -= 1
        elif key == pygame.K_RIGHT:
            x += 1
        elif key == pygame.K_UP:
            y -= 1
        elif key == pygame.K_DOWN:
            y += 1
        if TileMap.In((x, y), (TileMap.MapWidth, TileMap.MapHeight)):
            RollBack = MapCursorCoordinates
            if RollBack != (-1, -1):
                FirstKey = False
            MapCursorCoordinates = x, y
            MapCursor.Move((x,y), Cooldown, animation_type=1)
        else:
            return
        if key == pygame.K_LEFT and x < TileMap.MapX + MapCursorMargin[0]:
            TileMap.AnimatedMove((TileMap.MapX - 1, TileMap.MapY), Cooldown)
        elif key == pygame.K_RIGHT and x > TileMap.MapEndX() - MapCursorMargin[0]:
            TileMap.AnimatedMove((TileMap.MapX + 1, TileMap.MapY), Cooldown)
        elif key == pygame.K_UP and y < TileMap.MapY + MapCursorMargin[1]:
            TileMap.AnimatedMove((TileMap.MapX, TileMap.MapY - 1), Cooldown)
        elif key == pygame.K_DOWN and y > TileMap.MapEndY() - MapCursorMargin[1]:
            TileMap.AnimatedMove((TileMap.MapX, TileMap.MapY + 1), Cooldown)


def KeyUpHandler(key_delta):
    global MapCursorCoordinates, FirstKey
    if not FirstKey:
        if key_delta < Cooldown / 3:
            MapCursorCoordinates = RollBack
            MapCursor.Move(RollBack, key_delta)
    FirstKey = True


def CursorCoords():
    return MapCursorCoordinates