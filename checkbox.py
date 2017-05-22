import pygame
#from pygame.sprite import Sprite

class checkbox(object):
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image_unchecked = pygame.image.load('images/checkbox_empty.png')
        self.image_checked = pygame.image.load('images/checkbox_checked.png')
        self.rect = self.image_unchecked.get_rect()
        #self.width = 30
        #self.height = 30
        #self.button_color = 0, 200, 150
        #self.text_color = 255, 255, 255
        #self.font = pygame.font.Font(None, 52)
        #self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.toggledOn = False
        #self.setup_message(button_text)

    def toggle(self):
        if self.toggledOn == False:
            self.toggledOn = True
        else:
            self.toggledOn = False

    def draw_button(self):
        if self.toggledOn == True:
            self.screen.blit(source = self.image_checked, dest = self.rect)
        else:
            self.screen.blit(source = self.image_unchecked, dest = self.rect)
