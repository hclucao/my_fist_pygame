import pygame, json
import dirmestre
from pygame.locals import *

dm = dirmestre.Diretorio() #chamando a 

sprite_sheet = pygame.image.load(dm.perso()) #loading the spritesheet of the player

player_info = json.load(open(dm.perso_info())) #importando o json com as informaçoes do player

class Player(pygame.sprite.Sprite):
    def __init__(self):
        """todo que envolve o personagem
        """
        global word_movement, player_movement, playerect, gravity
        gravity = True
        word_movement = [0, 0] #movimentação do mundo
        player_movement = [0,0]
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
            img = pygame.transform.scale(img, (32*2, 32*2))
            self.imagens_dinossauro.append(img)

        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.rect = self.image.get_rect()
        playerect = self.rect

    def update(self):
        self.rect.center = (self.pos_x, self.pos_y)
        self.index_lista += 0.25
        if self.index_lista == 3: self.index_lista = 0
        self.image = self.imagens_dinossauro[int(self.index_lista)]

        #movimentacao
        if self.right and self.left == True:
            self.walkingr(0)
        else:
            if self.right == True:
                self.walkingr(64)
                if self.pos_x > 400:
                    word_movement[0] -= 4
                else:
                    player_movement[0] += 4
    
            ###self.left moviment
            if self.left == True:
                self.walkingr(96)
                if self.pos_x < 200:
                    word_movement[0] += 4
                else:
                    player_movement[0] -= 4
        ###self.up moviment
        if self.up == True:
            if self.pos_y > 100:
                player_movement[1] -= 10
            else:
                word_movement[1] += 10
                
        #gravidade
        if gravity:
            if self.pos_y < 410:
                player_movement[1] += 5
            else:
                word_movement[1] -= 5

        self.pos_x = player_movement[0]; self.pos_y = player_movement[1]

    def walkingr(self, index):
        """ metodo para atualização de sprite
        0 = parado para o lado direito
        1 = parado para o lado esquedo
        2 = andando para o lado direito
        3 = andando para o lado esquerdo
        """
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []
        self.lineY = index
        for i in range(1, 4):
            img = sprite_sheet.subsurface(( i * 32, self.lineY), (32,32))
            img = pygame.transform.scale(img, (32*2, 32*2))
            self.imagens_dinossauro.append(img)
