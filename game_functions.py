import sys

from time import sleep
import pygame

def check_events(config, sprites_list):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_mouse_button_down(event, config, sprites_list, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, config, sprites_list)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, config, sprites_list)

def check_mouse_button_down(event, config, sprites_list, mouse_x, mouse_y):
    """Respond to mouse button press."""
    pass

def check_keydown_events(event, config, sprites_list):
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
        # move the Wizard upwards.
        sprites_list.wiz.moving_up = True
    elif event.key == pygame.K_DOWN:
        # move the Wizard downwards.
        sprites_list.wiz.moving_down = True

def check_keyup_events(event, config, sprites_list):
    """Respond to key releases."""
    if event.key == pygame.K_UP:
        sprites_list.wiz.moving_up = False
    elif event.key == pygame.K_DOWN:
        sprites_list.wiz.moving_down = False

def update_screen(config, sprites_list):
    """Update images on the screen and flip to the new screen."""
    sprites_list.draw()
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Start a new game."""
    if not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True
        
        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

