import pygame
import player
import spritesheet as ss

#grama = ss.Grama()
#rect_grama = grama.get_rect()

class Word:
    def __init__(self) -> None:
        """
        toda a construção do mundo sera pósta aqui
        como o céu, chão... contruções no geral
        """
        self.word = pygame.Rect(0, 0, 1000,1000)
        self.tiles = [
            pygame.Rect(200, 300, 200, 30)
        ]
        #draw tiles by loop for
        self.blocks = [
            pygame.Rect(100,220, 50,50)
        ]

    def update(self, screen) -> None:
        """
        deve ser passado a tela em que
        tudo sera renderizado
        """
        pygame.draw.rect(screen, (255, 255, 255), self.word)
        for self.tile in self.tiles:
            pygame.draw.rect(screen, (50, 200, 0), self.tile)
        for block in self.blocks:
            block.copy()
            pygame.draw.rect(screen, (0,0,255), block) #draw tiles
        block.x += player.word_movement[0]; block.y += player.word_movement[1]
        self.word.x += player.word_movement[0]; self.word.y += player.word_movement[1]
        self.tile.x += player.word_movement[0]; self.tile.y += player.word_movement[1]
        player.word_movement = [0, 0]
        global tilerect
        tilerect = self.tile
