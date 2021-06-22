import pygame
from pygame.locals import *
import os

diretorioMestre = os.path.dirname(__file__) #definindo os diretorio para que essa script rode em qualquer pc
diretorioIMG = os.path.join(diretorioMestre, 'img') # aqui vamos comecar pelo diretorio principal e dps entrar na pasta img
diretorioSound = os.path.join(diretorioMestre, 'sound')

pygame.init()
screen = pygame.display.set_mode((640, 400))

clock = pygame.time.Clock()

pygame.display.set_caption('testes')

sprite_sheet = pygame.image.load(os.path.join(diretorioIMG, 'perso.png')).convert_alpha()

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []
        for i in range(1, 4):
            img = sprite_sheet.subsurface(( i * 32,32), (32,32))
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.imagens_dinossauro.append(img)

        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100,100)

    def update(self):
        self.index_lista += 0.25
        if self.index_lista == 3: self.index_lista = 0
        self.image = self.imagens_dinossauro[int(self.index_lista)]

todas_as_sptites = pygame.sprite.Group()
dino = Dino()
todas_as_sptites.add(dino)


running = True
while running:
    clock.tick(30)
    screen.fill((255,255,255))
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False

    todas_as_sptites.draw(screen)
    todas_as_sptites.update()

    pygame.display.update() # update the screen