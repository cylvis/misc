import sys
import pygame
import pygame.font
from pygame.locals import *
from pygame import Surface

def check_events(screen, game_settings, fullscreenCheckbox):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if fullscreenCheckbox.rect.collidepoint(mouse_x, mouse_y):
                fullscreenCheckbox.toggle()
                if fullscreenCheckbox.toggledOn == True:
                    screen = pygame.display.set_mode(game_settings.screen_size, FULLSCREEN)
                else:
                    screen = pygame.display.set_mode(game_settings.screen_size)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #Bring up the menu overlay
                if game_settings.main_menu_overlay == True:
                    game_settings.main_menu_overlay = False
                else:
                    game_settings.main_menu_overlay = True
            #else:
                #game_settings.game_active = True

def update_screen(screen, game_settings, fullscreenCheckbox):
    screen.fill(game_settings.bg_color)
    if game_settings.main_menu_overlay == True:
        drawMainMenuOverlay(screen, game_settings, fullscreenCheckbox)
    #if not game_settings.game_active:
        #fullscreenCheckbox.draw_button()
    pygame.display.flip()

def drawMainMenuOverlay(screen, game_settings, fullscreenCheckbox):
    overlay_width = game_settings.main_menu_font*12
    overlay_height = game_settings.main_menu_font*16
    overlay_bg_color = (30,30,30)
    overlay_rect = pygame.Rect((game_settings.screen_width/2)-(overlay_width/2), (game_settings.screen_height/2)-(overlay_height/2), overlay_width, overlay_height)
    screen.fill(overlay_bg_color, overlay_rect, BLEND_SUB)
    fullscreenCheckbox.draw_button()
