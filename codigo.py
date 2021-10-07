import pygame
from random import randint
pygame.init()

x = 230 # max 530 min 230
y = 100
pos_x = 526
pos_y = 800
pos_y_a = 1200
pos_y_c = 1600

velocidade_outros = 12

velocidade = 20
fundo = pygame.image.load('tela.jpeg')
boti = pygame.image.load('boti.PNG')
perfume1 = pygame.image.load('perfume1.png')
perfume2 = pygame.image.load('perfume2.png')
perfume3 = pygame.image.load('perfume3.png')

janela = pygame.display.set_mode((800,400))
pygame.display.set_caption("Jogo da Giovana Grupo boticario")
janela_aberta = True
while janela_aberta :
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False

        comandos = pygame.key.get_pressed()

        if comandos[pygame.K_RIGHT] and x<= 530:
            x += velocidade
        if comandos[pygame.K_LEFT] and x >= 230:
            x -= velocidade

        if (pos_y <= -180) and (pos_y_a <= -180) and (pos_y_c <= -180) :
            pos_y = randint(800,2000)
            pos_y_a = randint(800,2000)
            pos_y_c = randint(800,2000)

        pos_y -= velocidade_outros + randint(1,10)
        pos_y_a -= velocidade_outros + randint(1,10)
        pos_y_c -= velocidade_outros + randint(1,10)


        janela.blit(fundo,(0,0))
        janela.blit(boti,(x,y))
        janela.blit(perfume1, (pos_x, pos_y))
        janela.blit(perfume2, (pos_x  -300, pos_y_a))
        janela.blit(perfume3, (pos_x - 136, pos_y_c))
        pygame.display.update()

pygame.quit()