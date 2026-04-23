import pygame
from Globals import *
from sprite import Entity
from Player import Player
from TextureData import solo_texture_data, atlas_texture_data

class Scene:
    def __init__(self, app):
        self.app = app

        self.solo_textures = self.gen_solo_textures()
        self.atlas_textures = self.gen_atlas_texture_data('res/Textures-16.png')

        self.sprites = pygame.sprite.Group()
        self.entity = Entity([self.sprites], image=self.atlas_textures['dirt'])
        Entity([self.sprites], position=(100,100), image = self.solo_textures['player_static'])
        Entity([self.sprites], position=(200,200))

        self.gen_world()

    def gen_solo_textures(self):
        textures = {}
        for name, data in solo_texture_data.items():
            textures[name] = pygame.transform.scale(pygame.image.load(data['file_path']).convert_alpha(), (data['size']))

        return textures
    def gen_atlas_texture_data(self, filepath):
        textures = {}
        atlas_img = pygame.transform.scale(pygame.image.load(filepath).convert_alpha(), (TILESIZE*16, TILESIZE*16))

        for name, data in atlas_texture_data.items():
            textures[name] = pygame.Surface.subsurface(atlas_img, pygame.Rect(data['position'], data['size']))

        return textures
    def gen_world(self):
        pass
    def update(self):
        self.sprites.update()
    def draw(self):
        self.app.screen.fill('lightblue')
        self.sprites.draw(self.app.screen)