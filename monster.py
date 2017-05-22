import pygame
from pygame.sprite import Sprite

class Monster(Sprite):
    def __init__(self, screen, hero, game_settings):
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/monster.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def update(self):


    def draw_monster(self):
