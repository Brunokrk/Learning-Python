import sys

import pygame

def run_game():
    """Inicializa o jogo e cria um objeto na tela"""
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Space Invaders")

    #Inicializa o laço principal do jogo
    while True:

        #Observa eventos de teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  
        #Deixa a tela mais recente visível
        pygame.display.flip()

run_game()