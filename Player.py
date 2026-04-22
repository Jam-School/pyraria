import pygame
from Globals import *


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image=pygame.Surface((TILESIZE*2, TILESIZE*3)), position = (SCREENHEIGHT/2,SCREENWIDTH/2)):
        super().__init__(groups)
        self.image = image
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = position)
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= 1
        if keys[pygame.K_d]:
            self.rect.x += 1

    def update(self):
        self.input()
