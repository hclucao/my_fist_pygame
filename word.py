import pygame, dirmestre, player

class Word(player.Player):
    def __init__(self) -> None:
        """toda a construção do mundo sera pósta aqui
        como o céu, chão... contruções no geral
        """
        self.word = pygame.Rect(200, 200, 1000,1000)
        self.tile = pygame.Rect(280, 1150, 200, 30)
        #draw tiles by loop for
        self.blocks = [
            pygame.Rect(100,100, 50,50), pygame.Rect(160,100, 50,50),
            pygame.Rect(220, 100, 50, 50)
            ]

    def update(self, screen) -> None:
        """deve ser passado a tela em que
        tudo sera renderizado
        """
        player.Player.moviment(self) #herda atributos do metodo moviment, da class Player
        for block in self.blocks:
            block.copy()
            pygame.draw.rect(screen, (0,0,255), block) #draw tiles
        pygame.draw.rect(screen, (255, 255, 255), self.word)
        block.x += self.word_movement[0]; block.y += self.word_movement[1]
        self.word.x += self.word_movement[0]; self.word.y += self.word_movement[1]
        self.tile.x += self.word_movement[0]; self.tile.y += self.word_movement[1]