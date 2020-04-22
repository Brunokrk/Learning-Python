import pygame

from settings import Settings

from ship import Ship

import game_functions as gf

def run_game():
    """Inicializa o pygame, as configurações e o objeto screen"""

    #inicializa configurações de segundo plano necessárias ao pygame
    #para funcionar apropriadamente
    pygame.init()   

    #Instancia de settings para acessar configurações
    ai_settings = Settings()

    #cria janela de exibição
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #
    pygame.display.set_caption("Space Invaders")

    #Cria uma espaçonave
    ship = Ship(screen)


    #Inicializa o laço principal do jogo
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

        

run_game()
