import pygame
from pygame.locals import *
import dirmestre
from pygame import time

dm = dirmestre.Diretorio()

sprite_sheet = pygame.image.load(dm.perso()) #loading the spritesheet of the player

class Player(pygame.sprite.Sprite):
    def __init__(self):
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
    
    def moviment(self):
        """tem como propriedade listas que armazenam o posicionamento de objetos.\n
        com possibiladade de mudança de sues valores
        """
        self.word_movement = [0,0]

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)
        self.index_lista += 0.25
        if self.index_lista == 3: self.index_lista = 0
        self.image = self.imagens_dinossauro[int(self.index_lista)]

        #movimentacao
        self.moviment()
        player_movement = [0,0]
        if self.right and self.left == True:
            self.walkingr(0)
        else:
            if self.right == True:
                self.walkingr(32)
                if self.pos_x > 400:
                    self.word_movement[0] -= 5
                else:
                    player_movement[0] += 3; self.word_movement[0] -= 5
            else: self.walkingr(0)
            ###self.left moviment
            if self.left == True:
                self.walkingr(64)
                if self.pos_x < 200:
                    self.word_movement[0] += 5
                else:
                    player_movement[0] -= 3; self.word_movement[0] += 5
            ###self.up moviment
        if self.up == True:
            if self.pos_y > 100:
                player_movement[1] -= 10
            else:
                self.word_movement[1] += 10
                
        #gravidade  
        if self.pos_y < 410:
            self.pos_y += 5
        else:
            self.word_movement[1] -= 5

        self.pos_x += player_movement[0]; self.pos_y += player_movement[1]

    def walkingr(self, index):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []
        self.lineY = index
        for i in range(1, 4):
            img = sprite_sheet.subsurface(( i * 32,self.lineY), (32,32))
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.imagens_dinossauro.append(img)
