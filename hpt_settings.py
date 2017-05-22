import sys
import pygame
import pygame.font

class Settings():
    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 768
        self.screen_size = (self.screen_width, self.screen_height)
        self.bg_color = (82,111,53)
        #self.bullet_speed = 1
    	#self.bullet_width = 3
    	#self.bullet_height = 10
    	#self.bullet_color = 0, 0, 0
        self.game_active = False
        self.FRAMES_PER_SECOND = 30
        self.paused = False
        self.main_menu_overlay = True
        self.main_menu_font = pygame.font.Font(None, 24)
        self.main_menu_text_color = (0,0,0)
