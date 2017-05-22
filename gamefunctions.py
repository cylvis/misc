import sys
import pygame
from bullets import Bullet

def check_events(hero, bullets, game_settings, screen, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x, mouse_y):
                game_settings.game_active = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                hero.moving_right = True
            elif event.key == pygame.K_LEFT:
                hero.moving_left = True
            elif event.key == pygame.K_UP:
                hero.moving_up = True
            elif event.key == pygame.K_DOWN:
                hero.moving_down = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, hero, game_settings)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                hero.moving_right = False
            elif event.key == pygame.K_LEFT:
                hero.moving_left = False
            elif event.key == pygame.K_UP:
                hero.moving_up = False
            elif event.key == pygame.K_DOWN:
                hero.moving_down = False

def update_screen(settings, screen, hero, bullets, play_button):
    screen.fill(settings.bg_color)
    hero.draw_me()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    if not settings.game_active:
        play_button.draw_button()
    pygame.display.flip()
