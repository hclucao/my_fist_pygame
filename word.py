import pygame, player

class Word():
    def __init__(self) -> None:
        """toda a construção do mundo sera pósta aqui
        como o céu, chão... contruções no geral
        """
        self.word = pygame.Rect(200, 200, 1000,1000)
        self.tile = pygame.Rect(280, 200, 200, 30)
        #draw tiles by loop for
        self.blocks = [
            pygame.Rect(120,100, 50,50), pygame.Rect(300,100, 50,50),
            pygame.Rect(400, 100, 50, 50)
            ]

    def update(self, screen) -> None:
        """deve ser passado a tela em que
        tudo sera renderizado
        """
        pygame.draw.rect(screen, (255, 255, 255), self.word)
        pygame.draw.rect(screen, (32, 100, 150), self.tile)
        for block in self.blocks:
            pygame.draw.rect(screen, (0,0,255), block) #draw tiles
        block.x += player.word_movement[0]; block.y += player.word_movement[1]
        self.word.x = player.word_movement[0]; self.word.y = player.word_movement[1]
        self.tile.x += player.word_movement[0]; self.tile.y += player.word_movement[1]
        print(player.word_movement)