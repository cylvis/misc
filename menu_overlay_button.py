import pygame

class Menu_Overlay_Button(object):
    def __init__(self, screen, rect, button_text, font, text_color, text_color_MO, bg_color, bg_color_MO): # MO stands for mouseover
        self.screen = screen
        self.rect = rect
        self.button_text = button_text
        self.font = font
        self.text_color = text_color
        self.text_color_MO = text_color_MO
        self.bg_color = bg_color
        self.bg_color_MO = bg_color_MO
        self.setup_button()


    def setup_button(self):
        # Render text to images for highlighted and non-highlighted buttons
        self.button_image = self.font.render(self.button_text, True, self.text_color)
        self.button_image_MO = self.font.render(self.button_text, True, self.text_color_MO)
        # Center images on the rect provided in the __init__
        self.button_image_rect = self.button_image.get_rect()
        self.button_image_rect.center = self.rect.center
        self.button_image_MO_rect = self.button_image_MO.get_rect()
        self.button_image_MO_rect.center = self.rect.center


    # Draws the button taking into account whether or not the button is currently highlighted
    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            # If highlighted
            self.screen.fill(self.bg_color_MO, self.rect, pygame.BLEND_SUB)
            self.screen.blit(self.button_image_MO, self.button_image_MO_rect)
        else:
            # If not highlighted
            self.screen.fill(self.bg_color, self.rect, pygame.BLEND_SUB)
            self.screen.blit(self.button_image, self.button_image_rect)


    # Returns True if supplied coordinates are inside the button rectangle, otherwise returns False
    def left_click(self, mouse_x, mouse_y):
        if self.rect.collidepoint(mouse_x, mouse_y):
            return True
        else:
            return False
