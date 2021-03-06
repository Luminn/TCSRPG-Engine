
import pygame
import math
from Definitions.Align import *

def distance(v2):
    x,y = v2
    return math.sqrt(x * x + y * y)

# GameSprite but with pixels rather than tiles
class ScreenSprite(pygame.Surface):

    def __init__(self, image, slices=(0,0), frame=(0,0), scale=None, size=None):
        self.coords = (0,0) # tile map coords, not pixel coords
        self.alignment = ALIGN_DEFAULT
        if scale is not None:
            sx, sy = scale
            self.image = pygame.transform.scale(image, (image.get_width() * sx, image.get_height() * sy))
        elif size is not None:
            sx, sy = size
            self.image = pygame.transform.scale(image, (sx, sy))
        else:
            self.image = image
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.slices = slices if isinstance(slices, tuple) else (1, slices)
        self.width = self.image.get_width()/self.slices[0]
        self.height = self.image.get_height()/self.slices[1]
        self.frame = frame[0] % self.width, frame[1] % self.width
        pygame.Surface.__init__(self, (self.width, self.height), pygame.SRCALPHA)
        self.fill((0,0,0))
        self.set_colorkey((0,0,0))
        self.blit(self.image, (0,0), (self.frame[0] * self.width, self.frame[1] * self.height, self.width, self.height))
        self.visible = True
        self.animation_offset = (0,0)
        self.animation_speed = 0
        self.animation_distance = 0
        self.animation_type = 0
        self.frame_animation_target = None
        self.frame_animation_speed = 0

    def SetFrame(self, frame):
        self.fill((0,0,0))
        self.frame = frame[0] % self.slices[0], frame[1] % self.slices[1]
        self.blit(self.image, (0,0), (self.frame[0] * self.width , self.frame[1] * self.height, self.width, self.height))

    def GetCoords(self):
        return self.coords

    def SetCoords(self, coords):
        self.coords = coords

    def Alignment(self, option):
        self.alignment = option

    def SelfOffset(self):
        return self.animation_offset

    def Move(self, target, time=0, force_position=False, animation_type=1):
        if time == 0:
            self.coords = target
            return
        if force_position:  # forcefully reset animation offset
            self.animation_offset = 0
        x,y = self.coords
        tx, ty = target
        ox, oy = self.animation_offset
        self.animation_offset = ox + (x - tx), oy + (y - ty)
        self.animation_distance = distance(self.animation_offset)
        self.animation_speed = distance(self.animation_offset)/time
        self.animation_type = animation_type
        self.coords = target

    def Update(self, dt):
        #positional animation
        m = self.animation_speed * dt
        if self.animation_type == 2:
            accl = min(self.animation_distance - distance(self.animation_offset), distance(self.animation_offset))
            if accl < 5:
                m /= 2
        x, y = self.animation_offset
        d = math.sqrt(x * x + y * y)
        if d == 0 or self.animation_speed == 0:
            return
        x = math.copysign(abs(x - m * x/d) if x * (x - m * x/d) > 0 else 0, x)
        y = math.copysign(abs(y - m * y/d) if y * (y - m * y/d) > 0 else 0, y)
        self.animation_offset = x, y















