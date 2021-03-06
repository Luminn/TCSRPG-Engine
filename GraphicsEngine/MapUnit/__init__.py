from __future__ import annotations
from GraphicsEngine.GameSprite import GameSprite
from GraphicsEngine.Sprites import GetSprite

import pygame

class MapUnit(GameSprite):

    def __init__(self, unit):
        image = pygame.image.load(GetSprite(unit.info.sprite_index))
        GameSprite.__init__(self, image, 18, (0,0), (2,2))
        self.unit = unit
        self.unit.map_unit = self
        self.idle_start = 0
        self.idle_end = 2
        self.idle_time = 200
        self.anim_timer = 0
        self.idle_loop = True
        self.idle_modifier = 1

    def GetCoords(self):
        return self.unit.coords

    def SetCoords(self, coords):
        self.unit.coords = coords

    def Idle(self, dt):
        x,y = self.frame
        self.anim_timer += dt
        if self.anim_timer > self.idle_time:
            if self.idle_loop and (y > self.idle_end or y < self.idle_start):
                self.idle_modifier *= -1
            elif y >= self.idle_end:
                y = self.idle_start - 1
            y += self.idle_modifier
            self.anim_timer -= self.idle_time
            self.SetFrame((x,y))

    def Update(self, dt):
        GameSprite.Update(self, dt)
        self.Idle(dt)



