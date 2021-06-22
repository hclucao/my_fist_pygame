import pygame, dirmestre, player

class word(player.Player):
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

    def update(self) -> None:
        player.Player.update(self)
        for block in self.blocks:
            block.copy()
            block.x += self.word_movement[0]; block.y += self.word_movement[1]
        word.x += self.word_movement[0]; word.y += self.word_movement[1]
        self.tile.x += self.word_movement[0]; self.tile.y += self.word_movement[1]