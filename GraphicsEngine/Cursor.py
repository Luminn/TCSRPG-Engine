
from enum import Enum

# determines what the arrow keys control
import pygame

from GraphicsEngine.TileMap.MapCursor import KeyDownHandler, KeyUpHandler

KeyTimestamp = 0


class CursorOwners(Enum):
    No = 0 # don't use this unless loading
    TileMap = 1 # defaults to 1 on a map, pressing
    MainMenu = 2
    Hand = 3
    SettingsMenu = 4
    UnitMenu = 5
    Gallery = 6

CursorOwner = CursorOwners.TileMap

def GetCursorOwner():
    return CursorOwner

def SetCursorOwner(cursor_type:CursorOwners):
    global CursorOwner
    CursorOwner = cursor_type

def KeyLoop():
    global KeyTimestamp
    current_time = pygame.time.get_ticks()
    pressed = False
    key_delta = current_time - KeyTimestamp
    KeyTimestamp = current_time
    for key in (pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT):
        if pygame.key.get_pressed()[key]:
            KeyDownHandler(key, key_delta if not pressed else 0)
            pressed = True
    key_delta = current_time - KeyTimestamp
    if not pressed and key_delta > 20:
        KeyUpHandler(key_delta)