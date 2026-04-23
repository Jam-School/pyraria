import pygame
from Globals import *
from sprite import Entity
from Player import Player

class Scene:
    def __init__(self, app):
        self.app = app

        player_texture = pygame.image.load('res/Placeholder.png').convert_alpha()
        player_texture = pygame.transform.scale(player_texture, TILESIZE, TILESIZE)

        self.sprites = pygame.sprite.Group()
        self.entity = Entity([self.sprites])
        Entity([self.sprites], position=(100,100), image = player_texture)
        Entity([self.sprites], position=(200,200))

        self.player = Player((self.sprites))
    def update(self):
        self.sprites.update()
    def draw(self):
        self.app.screen.fill('lightblue')
        self.sprites.draw(self.app.screen)