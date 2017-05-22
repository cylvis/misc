import sys, pygame
from pygame.locals import *
from hpt_settings import Settings
from checkbox import checkbox
import hpt_functions as functions

def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    game_settings = Settings()
    #message = input("Start Game:")
    screen = pygame.display.set_mode(game_settings.screen_size)
    pygame.display.set_caption("HPT - Test1")
    #hero = Hero(screen)
    #bullets = Group()
    #play_button = Play_button(screen, message)
    fullscreenCheckbox = checkbox(screen)




    while 1:
        clock.tick(game_settings.FRAMES_PER_SECOND)
        functions.check_events(screen, game_settings, fullscreenCheckbox)
        functions.update_screen(screen, game_settings, fullscreenCheckbox)
        #if game_settings.game_active:
            #hero.update()
            #bullets.update()
            #for bullet in bullets:
                #if bullet.rect.bottom <= 0:
                    #bullets.remove(bullet)
                #if len(bullets) > 15:
                    #bullets.remove(bullet)
run_game()
