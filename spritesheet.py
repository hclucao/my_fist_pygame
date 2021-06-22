import pygame
from pygame.locals import *
import dirmestre

dm = dirmestre.Diretorio()

sprite_sheet = pygame.image.load(dm.perso())

class Player(pygame.sprite.Sprite):
    def __init__(self,left, right, up):
        self.left = left
        self.right = right
        self.up = up
        self.pos_x = 300
        self.pos_y = 300
        self.forceJump = 5
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []
        self.lineY = 0
        for i in range(1, 4):
            img = sprite_sheet.subsurface(( i * 32,self.lineY), (32,32))
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.imagens_dinossauro.append(img)

        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.rect = self.image.get_rect()

    def update(self, ):
        self.rect.center = (self.pos_x, self.pos_y) #position of the player
        self.index_lista += 0.25
        if self.index_lista == 3: self.index_lista = 0
        self.image = self.imagens_dinossauro[int(self.index_lista)]
        #movimentacao

        player_movement = [0, 0]
        if self.right == True:
            player_movement[0] += 5
            self.walkingr(32)
        else : self.walkingr(0)
        if self.left == True:
            player_movement[0] -= 5
            self.walkingr(0)
        if self.up == True:
            player_movement[1] -= 10
        ###gravidade simples
        
        if self.pos_y >= 410:
            pass
        else:
            self.pos_y += 5
        

        self.pos_x += player_movement[0]
        self.pos_y += player_movement[1]

        self.scroll = [0, 0]
        """
        self.player_scroll_rect = self.rect.copy()
        self.player_scroll_rect.x -= self.scroll[0]
        self.player_scroll_rect.y -= self.scroll[1]

        self.scroll[0] += (self.pos_x - self.scroll[0] - (windowsize[0]/2)) // 20
        self.scroll[1] += (self.pos_y - self.scroll[1] - (windowsize[1]/2)) // 20
        """
    def walkingr(self, index):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []
        self.lineY = index
        for i in range(1, 4):
            img = sprite_sheet.subsurface(( i * 32,self.lineY), (32,32))
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.imagens_dinossauro.append(img)