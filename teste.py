import pygame as pg
import dirmestre
import os

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Ball(pg.sprite.Sprite):

    def __init__(self, pos):
        super(Ball, self).__init__()
        self.image = pg.image.load(os.path.join('img', 'grama.png'))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        pass


# Initialise pygame
pg.init()

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Create sprites
ball = Ball((100, 200))
group = pg.sprite.RenderPlain()
group.add(ball)

# Main loop, run until window closed
running = True
while running:

    # Check events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))
    group.draw(screen)
    pg.display.flip()

# close pygame
pg.quit()