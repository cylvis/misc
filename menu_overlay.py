import pygame
from menu_overlay_button import Menu_Overlay_Button

class Menu_Overlay(object):
    def __init__(self, screen, font, text_color, text_color_MO, bg_color, bg_color_MO, menu_choices, paddingX, paddingY): # MO stands for mouseover
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        self.font = font
        self.text_color = text_color
        self.text_color_MO = text_color_MO
        self.bg_color = bg_color
        self.bg_color_MO = bg_color_MO
        self.menu_choices = menu_choices
        self.rows = len(menu_choices)
        self.paddingX = paddingX
        self.paddingY = paddingY

        #Determine menu pixel size
        self.row_height = pygame.font.Font.get_height(self.font) + self.paddingY
        self.menu_width = 0
        for i in range(0, self.rows): # Find the longest menu string
            row_size = pygame.font.Font.size(self.font, menu_choices[i])
            if row_size[0] > self.menu_width:
                self.menu_width = row_size[0]
        self.menu_width = self.menu_width + self.paddingX
        self.menu_height = self.row_height * self.rows

        self.rect = pygame.Rect((self.screen_width/2)-(self.menu_width/2), (self.screen_height/2)-(self.menu_height/2), self.menu_width, self.menu_height)

        #Create rects for each menu choice
        self.button_rects = []
        for i in range(0, self.rows):
            self.button_rects.append(pygame.Rect((self.screen_width/2)-(self.menu_width/2), (self.screen_height/2)-(self.menu_height/2)+(i*self.row_height), self.menu_width, self.row_height))

        #Create buttons for each menu choice
        self.buttons = []
        for i in range(0, self.rows):
            self.buttons.append(Menu_Overlay_Button(self.screen, self.button_rects[i], self.menu_choices[i], self.font, self.text_color, self.text_color_MO, self.bg_color, self.bg_color_MO))


    def draw(self):
        for i in range(0, self.rows):
            self.buttons[i].draw()


    # Returns the number of the menu choice selected at the supplied coordinates, if none exists, returns None
    def left_click(self, mouse_x, mouse_y):
        if self.rect.collidepoint(mouse_x, mouse_y):
            for i in range(0, self.rows):
                if self.buttons[i].left_click(mouse_x, mouse_y):
                    return i
        else:
            return None
