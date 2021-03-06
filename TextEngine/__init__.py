
import Definitions.Colors as Colors
from GraphicsEngine.Sprites import GetSprite
import pygame

ColorDefinitions  = {
    "red": Colors.RED,
    "orange": Colors.ORANGE,
    "gold": Colors.GOLD,
    "green": Colors.GREEN,
    "blue": Colors.BLUE,
    "Purple": Colors.PURPLE
}



class DescriptionText:

    def __init__(self, string):
        self.Parse(string)


    def Parse(self, string):
        pass
