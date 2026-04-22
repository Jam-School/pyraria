import pygame
from Globals import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups, image = pygame.surface((TILESIZE, TILESIZE)), position = (0,0)):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft = position)


    def update(self):
        self.rect.x += 1

