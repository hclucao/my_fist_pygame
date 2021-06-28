import pygame
from dirmestre import Diretorio as dm

class Sprite(object):
    def __init__(self) -> str:
        self.img_grama = pygame.image.load(dm.grama())

    def get_grama(self):
        # Create a new blank image
        image = pygame.Surface([32, 16]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.img_grama, (0, 0), (32, 16, 32, 16))

        # Assuming black works as the transparent color
        image.set_colorkey(0,0,0)

        return image