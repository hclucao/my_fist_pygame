from pygame.locals import *
from sys import exit
import dirmestre, player, word, coliders
import pygame

pygame.init()
pygame.mixer.init()

#tamanho da tela
windowsize = (640, 480)
screen = pygame.display.set_mode((windowsize))

#name of the screen
pygame.display.set_caption('gg izi game')

#import module
dm = dirmestre.Diretorio()
player = player.Player()
word = word.Word()

#call the module
fps = pygame.time.Clock() #loading component for limit the fps

"""
adicionando as sprites no grupo, assim todas seram desenhadas
sem ter que definir separadamente a tela em que sera feito

"""
todas_as_sptites = pygame.sprite.Group()
todas_as_sptites.add(player)
todas_as_sptites.add(word)

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
                player.walkingr(0)
            if event.key == K_a:
                player.left = False
                player.walkingr(32)
            if event.key == K_w:
                player.up = False

    #update
    player.update()
    word.update(screen)
    coliders.Colider()

    #draw
    todas_as_sptites.draw(screen)
    todas_as_sptites.update()

    #isso faz com que o game seja atualizado a cada frame
    pygame.display.flip()