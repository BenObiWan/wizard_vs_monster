import pygame
from pygame.sprite import Sprite

class Wizard(Sprite):
    """A class representing the Wizard"""

    def __init__(self, config, sprites_list):
        """Initialize the wizard."""
        super().__init__()
        self.config = config
        self.sprites_list = sprites_list
        self.screen = sprites_list.screen

        # load the wizard's image
        self.image = pygame.image.load('images/wizard.png')
        self.rect = self.image.get_rect()
        self.screen_rect = sprites_list.screen.get_rect()

        # starting position for the wizard
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value for the wizard's center.
        self.center = float(self.rect.centery)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

        # Starting magic missile settings
        self.magic_missile_width = config.start_magic_missile_width
        self.magic_missile_heigth = config.start_magic_missile_heigth
        self.magic_missile_color = config.start_magic_missile_color
        self.magic_missile_allowed = config.start_magic_missile_allowed
        self.magic_missile_speed_factor = config.start_magic_missile_speed_factor

    def update(self):
        """Update the wizard's position based on the movement flag."""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= self.config.wizard_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.config.wizard_speed_factor
        # Update rect object from self.center.
        self.rect.centery = self.center

    def blitme(self):
        """Draw the wizard at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_wizard(self):
        """Center the wizard on the screen."""
        self.center = self.screen_rect.centery


