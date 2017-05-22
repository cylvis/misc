import sys, pygame
from hero import Hero
from settings import Settings
import gamefunctions as gf
from pygame.sprite import Group
from start_button import Play_button


def run_game():
    pygame.init()
    game_settings = Settings()
    message = "Start Game:"
    screen = pygame.display.set_mode(game_settings.screen_size)
    pygame.display.set_caption("Monster Attack")
    hero = Hero(screen)
    bullets = Group()
    play_button = Play_button(screen, message)

    while 1:
        gf.check_events(hero, bullets, game_settings, screen, play_button)
        gf.update_screen(game_settings, screen, hero, bullets, play_button)
        if game_settings.game_active:
            hero.update()
            bullets.update()
            for bullet in bullets:
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
                if len(bullets) > 15:
                    bullets.remove(bullet)
run_game()
