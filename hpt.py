import sys, pygame
from pygame.locals import *
from hpt_settings import Settings
from checkbox import checkbox
from menu_overlay import Menu_Overlay
import hpt_functions as functions

def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    settings = Settings()
    #message = input("Start Game:")
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption("HPT - Test1")
    #hero = Hero(screen)
    #bullets = Group()
    #play_button = Play_button(screen, message)
    fullscreenCheckbox = checkbox(screen)
    mainMenuChoices = ["Game Settings", "Audio/Video", "Exit"]
    mainMenu = Menu_Overlay(screen, settings.menu_font, settings.menu_text_color, settings.menu_text_color_MO, settings.menu_bg_color, settings.menu_bg_color_MO, mainMenuChoices, settings.menu_paddingX, settings.menu_paddingY)
    avMenuChoices = ["Toggle Fullscreen", "Back"]
    avMenu = Menu_Overlay(screen, settings.menu_font, settings.menu_text_color, settings.menu_text_color_MO, settings.menu_bg_color, settings.menu_bg_color_MO, avMenuChoices, settings.menu_paddingX, settings.menu_paddingY)




    while 1:
        clock.tick(settings.FRAMES_PER_SECOND)
        functions.check_events(screen, settings, mainMenu, avMenu)
        functions.update_screen(screen, settings, mainMenu, avMenu)
        #if game_settings.game_active:
            #hero.update()
            #bullets.update()
            #for bullet in bullets:
                #if bullet.rect.bottom <= 0:
                    #bullets.remove(bullet)
                #if len(bullets) > 15:
                    #bullets.remove(bullet)
run_game()
