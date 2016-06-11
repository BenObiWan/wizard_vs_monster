import pygame
from pygame.sprite import Sprite

class MagicMissile(Sprite):
    """A class to manage magic missiles sent by the wizard."""

    def __init__(self, config, sprites_list):
        """Create a magic missile at the wizard current position."""
        super().__init__()
        self.screen = sprites_list.screen

        self.magic_missile_width = sprites_list.wiz.magic_missile_width
        self.magic_missile_heigth = sprites_list.wiz.magic_missile_heigth
        self.color = sprites_list.wiz.magic_missile_color
        self.speed_factor = sprites_list.wiz.magic_missile_speed_factor

        # Create a missile rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.magic_missile_width,
                               self.magic_missile_heigth)
        self.rect.centery = sprites_list.wiz.rect.centery
        self.rect.right = sprites_list.wiz.rect.right

        # Store the missile's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):
        """Move the missile right."""
        # Update the decimal position of the bullet.
        self.x += self.speed_factor
        # Update the rect position.
        self.rect.x = self.x

    def draw_missile(self):
        """Draw the missile to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

