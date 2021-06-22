import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

pygame.display.set_caption("Scrolling example")
WINDOW_SIZE = (600, 400)
screen = pygame.display.set_mode(WINDOW_SIZE)

scroll = [0, 0]
player = pygame.Rect(100, 100, 10, 10)
up = False
down = False
left = False
right = False

blocks = [pygame.Rect(250,250,50,50)]

while True:
    screen.fill((0, 0, 0))

    scroll[0] += (player.x - scroll[0] - (WINDOW_SIZE[0]/2)) // 20
    scroll[1] += (player.y - scroll[1] - (WINDOW_SIZE[1]/2)) // 20

    player_movement = [0, 0]
    if right == True:
        player_movement[0] += 2
    if left == True:
        player_movement[0] -= 2
    if up == True:
        player_movement[1] -= 2
    if down == True:
        player_movement[1] += 2

    player.x += player_movement[0]
    player.y += player_movement[1]

    player_scroll_rect = player.copy()
    player_scroll_rect.x -= scroll[0]
    player_scroll_rect.y -= scroll[1]

    pygame.draw.rect(screen, (255,255,255), player_scroll_rect)

    
    for block in blocks:
        scroll_block = block.copy()
        scroll_block.x = scroll_block.x - scroll[0]
        scroll_block.y = scroll_block.y - scroll[1]
        pygame.draw.rect(screen, (0,0,255), scroll_block)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                right = True
            if event.key == K_LEFT:
                left = True
            if event.key == K_UP:
                up = True
            if event.key == K_DOWN:
                down = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                right = False
            if event.key == K_LEFT:
                left = False
            if event.key == K_UP:
                up = False
            if event.key == K_DOWN:
                down = False

    pygame.display.flip()
    clock.tick(60)