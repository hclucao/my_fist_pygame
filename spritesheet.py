import pygame
import dirmestre

dm = dirmestre.Diretorio()

class Grama(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(dm.grama())
        largura = 32
        altura = 16
        self.grama = img.subsurface((32, 16), (32, 16))
        return self.grama
