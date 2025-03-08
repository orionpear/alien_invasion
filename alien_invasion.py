import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """Initialize pygame, settings and a screen object."""
    pygame.init() #(func_desc) Initializes background settings that Pygame needs to work properly
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) #(func_desc) Creates a display window called a screen
    pygame.display.set_caption("Alien Invation")

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(
        ai_settings, screen,
        ship, aliens)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        gf.check_events(
            ai_settings, screen,
            ship, bullets)
        ship.update()
        gf.update_bullets(
            ai_settings, screen,
            ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        # Update the screen
        gf.update_screen(
            ai_settings, screen, ship,
              aliens, bullets)
    
run_game()
