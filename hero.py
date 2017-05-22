import pygame

class Hero(object):
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/hero.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 10
            print self.rect.centerx
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 10
            print self.rect.centerx

    def draw_me(self):
        self.screen.blit(source = self.image, dest = self.rect)
