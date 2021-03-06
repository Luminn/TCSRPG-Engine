
import pygame
from Definitions.Directories import BACKGROUND_FOLDER,MAP_FOLDER

BackGround = pygame.image.load(BACKGROUND_FOLDER + "main.jpg")

def BackgroundLoop(screen):
    screen.fill((0,0,0))
    screen.blit(BackGround, (0,0))