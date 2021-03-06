
import pygame
from GraphicsEngine.GameSprite import *
from GraphicsEngine.TileMap.DrawUnits import GetUnitsSprites
from Definitions.Directories import MAP_FOLDER, MAP_SPRITE_FOLDER
from Settings import Resolution_X, Resolution_Y
from typing import Set

# from settings
TileSize = 32                   # width and height of a square tile in pixel
ScreenTileWidth = Resolution_X // TileSize            # size of screen,not in pixel
ScreenTileHeight = Resolution_Y // TileSize

# set by map
MapWidth, MapHeight = 0, 0      # number of tiles in the map
MapX, MapY = 0, 0               # Current tile, used for game engine related stuff
MapOffsetPX = (0, 0, 0, 0)        # None tiled portion of the map
ScreenOffsetPX = (0, 0)

AnimationOffsetPX = (0, 0)        # will go to 0,0 with animation speed, in pixel
AnimationSpeedPX = .2              # pixels per .01 second

def In(coords, max_coords, min_coords=(0,0)):
    x,y = coords
    maxx, maxy = max_coords
    minx, miny = min_coords
    return minx <= x < maxx and miny <= y < maxy


def MapEndX():
    return MapX + ScreenTileWidth

def MapEndY():
    return MapY + ScreenTileHeight


MapImage:pygame.Surface = None

def ScreenPositionMax():
    x,y  = MapWidth - (Resolution_X - MapOffsetPX[2]) // TileSize, MapHeight - (Resolution_Y - MapOffsetPX[3]) // TileSize
    return  0 if x < 0 else x, 0 if y < 0 else y

def SetScreenPosition(coords):
    global MapX, MapY
    x,y = coords
    mx,my = ScreenPositionMax()
    MapX, MapY = x if x < mx else mx, y if y < my else my

def LoadMap(image, map_offset=(0,0,0,0)):
    global MapImage, MapWidth, MapHeight, MapOffsetPX, ScreenOffsetPX
    MapImage = pygame.image.load(MAP_FOLDER + image)
    MapImage = pygame.transform.scale(MapImage, (MapImage.get_width() * 2, MapImage.get_height() * 2))
    MapOffsetPX = map_offset
    MapWidth = (MapImage.get_width() - MapOffsetPX[0] - MapOffsetPX[2]) // TileSize
    MapHeight = (MapImage.get_height() - MapOffsetPX[1] - MapOffsetPX[3]) // TileSize
    ScreenOffsetPX = (0,0)



LoadMap("test.png")

#SetScreenPosition((9,11))

def AnimatedMove(position, time):
    global AnimationSpeedPX, AnimationOffsetPX, MapX, MapY, ScreenOffsetPX
    if not In(position, (MapWidth - ScreenTileWidth + 1, MapHeight - ScreenTileHeight + 1)):
        return #TODO: implement oob
    x, y = position
    a0, b0 = ScreenOffsetPX
    a, b = (MapWidth - x) * TileSize - Resolution_X, (MapHeight - y) * TileSize - Resolution_Y
    a, b = a if a < 0 else 0, b if b < 0 else 0
    ScreenOffsetPX = a, b
    AnimationOffsetPX = -(x - MapX) * TileSize - (a - a0), -(y - MapY) * TileSize - (b - b0)
    AnimationSpeedPX = distance(AnimationOffsetPX) / time
    MapX, MapY = x, y


def MapMove(dt):
    global AnimationOffsetPX
    offsetx, offsety = AnimationOffsetPX
    d = math.sqrt(offsetx * offsetx + offsety * offsety)
    if d == 0 or dt == 0:
        return
    m = AnimationSpeedPX * dt

    x = math.copysign(abs(offsetx - m * offsetx/d) if offsetx * (offsetx - m * offsetx/d) > 0 else 0, offsetx)
    y = math.copysign(abs(offsety - m * offsety/d) if offsety * (offsety - m * offsety/d) > 0 else 0, offsety)

    AnimationOffsetPX = x, y


def MapLoop(screen, dt):
    MapMove(dt)
    game_map = pygame.Surface((Resolution_X, Resolution_Y))
    game_map.blit(MapImage, (0,0), (MapX * TileSize + ScreenOffsetPX[0] + AnimationOffsetPX[0],
                                   MapY * TileSize + ScreenOffsetPX[1] + AnimationOffsetPX[1], Resolution_X, Resolution_Y))
    screen.blit(game_map, (0,0))

sprite = GameSprite(pygame.image.load(MAP_SPRITE_FOLDER + "Eirika.png"), 15)

TiledSprites:Set[GameSprite] = set()

#TiledSprites.add(sprite)

def GetDisplayedCoords(coords):
    x,y = coords
    a,b = AnimationOffsetPX
    c,d = ScreenOffsetPX
    return (x-MapX) * TileSize - c - a, (y-MapY) * TileSize - d - b

def MapObjectLoop(screen, dt):
    for i in GetUnitsSprites():
        i.Update(dt)
        if i.visible:
            a,b = GetDisplayedCoords(i.GetCoords())
            c,d = i.SelfOffset()
            screen.blit(i, (a+c, b+d))
    for i in TiledSprites:
        i.Update(dt)
        if i.visible:
            a,b = GetDisplayedCoords(i.GetCoords())
            c,d = i.SelfOffset()
            screen.blit(i, (a+c, b+d))



