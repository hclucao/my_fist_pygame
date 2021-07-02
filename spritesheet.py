import pygame, os
from pygame import sprite
from dirmestre import Diretorio as dm

#global variabes
grama = pygame.image.load(os.path.join('img', 'grama.png'))

class Sprite(sprite.Sprite):
    def __init__(self) -> str:
        sprite.Sprite.__init__(self)
        self.grama_rect = grama.get_rect()
        self.pos_itens = (200, 200)
        self.grama_rect.center = (self.pos_itens)
        self.group = pygame.sprite.RenderPlain()
        self.group.add(grama)
    def update(self, screen):
        self.group.draw(screen)
    def get_grama(self):
        # Create a new blank image
        pass