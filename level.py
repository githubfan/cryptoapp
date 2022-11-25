import pygame

class Level:
    def __init__(self):

        #Sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
    
    def run(self):
        #game update and draw
        pass