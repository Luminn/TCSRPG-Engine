
import pygame
import pygame.time
import pygame.freetype

from GraphicsEngine.Cursor import KeyLoop
from Settings import Resolution_X, Resolution_Y
from GraphicsEngine.TileMap.Background import BackgroundLoop
from GraphicsEngine.TileMap.ColoredOverlay import RangeDisplayLoop
from GraphicsEngine.TileMap import MapLoop, MapObjectLoop
from GraphicsEngine.TileMap.MapCursor import KeyDownHandler, KeyUpHandler
from GraphicsEngine.Cursor import KeyLoop
from GraphicsEngine.TileMap.UI import MapUiLoop
from GraphicsEngine.Menu import MenuLoop
from GraphicsEngine.KeyEvents import HandleClick, HandleSecondaryClick


KeyPressedTimestamp = 0
keyPressedDeltaTimeThreshold = 10
def KeyPressedLoop(key):
    if key == pygame.K_x:
        HandleClick()
    elif key == pygame.K_z:
        HandleSecondaryClick()

MaxFrameRate = 144

def Main():
    pygame.init()
    pygame.freetype.init()
    screen = pygame.display.set_mode((Resolution_X, Resolution_Y))
    pygame.display.set_caption("Cyruis Engine")
    clock = pygame.time.Clock()
    game_end = False

    while not game_end:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end = True
            elif event.type == pygame.KEYDOWN:
                KeyPressedLoop(event.key)

        KeyLoop()
        BackgroundLoop(screen)
        MapLoop(screen, dt)
        MapUiLoop(screen)
        RangeDisplayLoop(screen)
        MenuLoop(screen, dt)
        MapObjectLoop(screen, dt)
        pygame.display.update()

    pygame.quit()
    quit()