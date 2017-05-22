import pygame

class Settings():
    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 768
        self.screen_size = (self.screen_width, self.screen_height)
        self.bg_color = (120,120,180)
        self.game_active = False
        self.FRAMES_PER_SECOND = 30
        self.paused = False
        self.fullscreen = False
        self.main_menu_overlay = ""
        self.menu_font = pygame.font.Font(None, 36)
        self.menu_text_color = (0,0,0)
        self.menu_text_color_MO = (255,255,255)
        self.menu_bg_color = (30,30,30)
        self.menu_bg_color_MO = (50,50,50)
        self.menu_paddingX = 24
        self.menu_paddingY = 10
