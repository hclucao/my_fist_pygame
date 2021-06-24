from pygame import time
from pygame.locals import *
from sys import exit
import dirmestre, player, word
import pygame, os

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
player = player.Player()
word = word.Word()

#call the module
fps = pygame.time.Clock() #loading a component for limit of the fps

todas_as_sptites = pygame.sprite.Group()
todas_as_sptites.add(player)

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
                player.right = True
            if event.key == K_a:
                player.left = True
            if event.key == K_w:
                player.up = True
        #
        if event.type == KEYUP:
            if event.key == K_d:
                player.right = False
            if event.key == K_a:
                player.left = False
            if event.key == K_w:
                player.up = False


    player.update()
    word.update(screen)

    #draw
    todas_as_sptites.draw(screen)
    todas_as_sptites.update()

    #isso faz com que o game seja atualizado a cada frame
    pygame.display.flip()