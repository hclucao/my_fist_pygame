from pygame import time
from pygame.locals import *
from sys import exit
import dirmestre
import pygame
import os


pygame.init()
pygame.mixer.init()

#tamanho da tela
largura = 640
altura = 480
windowsize = (640, 480)
screen = pygame.display.set_mode((windowsize))

#name of the screen
pygame.display.set_caption('gg izi game')

#import module
dm = dirmestre.Diretorio()

#call the module
sprite_sheet = pygame.image.load(dm.perso()) #loading the spritesheet of the player
fps = pygame.time.Clock() #loading a component for limit of the fps

word = pygame.Rect(200, 200, 1000,1000)
tile = pygame.Rect(280, 1150, 200, 30)

#test of draw tiles by loop for
blocks = [pygame.Rect(100,100, 50,50), pygame.Rect(160,100, 50,50),
        pygame.Rect(220, 100, 50, 50)
        ]

class Player(pygame.sprite.Sprite):
    def __init__(self,):
        """todo que envolve o personagem
        """
        self.left = False
        self.right = False
        self.up = False
        self.pos_x = 300
        self.pos_y = 300
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []
        self.lineY = 0
        for i in range(1, 4):
            img = sprite_sheet.subsurface(( i * 32,self.lineY), (32,32))
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.imagens_dinossauro.append(img)

        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)
        self.index_lista += 0.25
        if self.index_lista == 3: self.index_lista = 0
        self.image = self.imagens_dinossauro[int(self.index_lista)]

        #movimentacao
        player_movement = [0,0]
        word_movement = [0,0]
        if self.right and self.left == True:
            self.walkingr(0)
        else:
            if self.right == True:
                self.walkingr(32)
                if self.pos_x > 400:
                    word_movement[0] -= 5
                else:
                    player_movement[0] += 3; word_movement[0] -= 5
            else: self.walkingr(0)
            ###self.left moviment
            if self.left == True:
                self.walkingr(64)
                if self.pos_x < 200:
                    word_movement[0] += 5
                else:
                    player_movement[0] -= 3; word_movement[0] += 5
            ###self.up moviment
        if self.up == True:
            if self.pos_y > 100:
                player_movement[1] -= 10
            else:
                word_movement[1] += 10
                
        #gravidade  
        if self.rect.colliderect(tile):
            pass
        else:
            if self.pos_y < 410:
                self.pos_y += 5
            else:
                word_movement[1] -= 5
        
        self.pos_x += player_movement[0]; self.pos_y += player_movement[1]
        word.x += word_movement[0]; word.y += word_movement[1]
        tile.x += word_movement[0]; tile.y += word_movement[1]

        for block in blocks:
            block.copy()
            block.x += word_movement[0]; block.y += word_movement[1]
            pygame.draw.rect(screen, (25,100,25), block)

    def walkingr(self, index):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []
        self.lineY = index
        for i in range(1, 4):
            img = sprite_sheet.subsurface(( i * 32,self.lineY), (32,32))
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.imagens_dinossauro.append(img)
            

todas_as_sptites = pygame.sprite.Group()
lucas = Player()
todas_as_sptites.add(lucas)


def updadeGeral():
    lucas.update()

    #draw
    pygame.draw.rect(screen, (255, 255, 255), word)
    pygame.draw.rect(screen, (25, 255, 25), tile)
    todas_as_sptites.draw(screen)
    todas_as_sptites.update()


while True:
    fps.tick(25)

    #isso tem a responsa de fazer a tela n ficar borrada com o rastro dos movimentos dos objs
    screen.fill((0,0,0))

    #esse for vai checar quando alguma coisa acontecer
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        #
        if event.type == KEYDOWN:
            if event.key == K_d:
                lucas.right = True
            if event.key == K_a:
                lucas.left = True
            if event.key == K_w:
                lucas.up = True
        #
        if event.type == KEYUP:
            if event.key == K_d:
                lucas.right = False
            if event.key == K_a:
                lucas.left = False
            if event.key == K_w:
                lucas.up = False

    updadeGeral()

    #isso faz com que o game seja atualizado a cada frame
    pygame.display.flip()