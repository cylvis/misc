import sys
import pygame
import pygame.font
from pygame.locals import *
from pygame import Surface

def check_events(screen, settings, mainMenu, avMenu):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if settings.main_menu_overlay == "main_menu":
                menuChoice = mainMenu.left_click(mouse_x, mouse_y)
                if menuChoice == 0:
                    # Open Game Settings
                    menuChoice = 0 # Because line cannot be blank
                elif menuChoice == 1:
                    # Open Audio/Video
                    settings.main_menu_overlay = "audio/video"
                elif menuChoice == 2:
                    sys.exit()
            elif settings.main_menu_overlay == "audio/video":
                menuChoice = avMenu.left_click(mouse_x, mouse_y)
                if menuChoice == 0:
                    if settings.fullscreen == False:
                        screen = pygame.display.set_mode(settings.screen_size, FULLSCREEN)
                        settings.fullscreen = True
                    else:
                        screen = pygame.display.set_mode(settings.screen_size)
                        settings.fullscreen = False
                elif menuChoice == 1:
                    settings.main_menu_overlay = "main_menu"
                    return

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #Bring up the menu overlay
                if settings.main_menu_overlay == "":
                    settings.main_menu_overlay = "main_menu"
                elif settings.main_menu_overlay == "main_menu":
                    settings.main_menu_overlay = ""
                elif settings.main_menu_overlay == "audio/video":
                    settings.main_menu_overlay = "main_menu"
                elif settings.main_menu_overlay == "game_settings":
                    settings.main_menu_overlay = "main_menu"
                #else:
                    #settings.game_active = True

def update_screen(screen, settings, mainMenu, avMenu):
    screen.fill(settings.bg_color)
    if settings.main_menu_overlay == "main_menu":
        mainMenu.draw()
    elif settings.main_menu_overlay == "audio/video":
        avMenu.draw()
        #fullscreenCheckbox.draw_button()
    #if not settings.game_active:
        #fullscreenCheckbox.draw_button()
    pygame.display.flip()

#def drawMainMenuOverlay(screen, settings, fullscreenCheckbox, mainMenuOverlay):
    #overlay_width = settings.main_menu_font*12
    #overlay_height = settings.main_menu_font*16
    #overlay_bg_color = (30,30,30)
    #overlay_rect = pygame.Rect((settings.screen_width/2)-(overlay_width/2), (settings.screen_height/2)-(overlay_height/2), overlay_width, overlay_height)
    #screen.fill(overlay_bg_color, overlay_rect, BLEND_SUB)
    #fullscreenCheckbox.draw_button()
