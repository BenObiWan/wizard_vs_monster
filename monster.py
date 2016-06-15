import pygame
from pygame.sprite import Sprite

class Monster(Sprite):
    """A class to represent a monster."""

    def __init__(self, config, sprites_list):
        """Initialize the monster and set its starting position."""
        super().__init__()
        self.config = config
        self.sprites_list = sprites_list
        self.screen = sprites_list.screen

        # load the zombie's image
        self.image = pygame.image.load('images/zombie.png')
        self.rect = self.image.get_rect()
        self.screen_rect = sprites_list.screen.get_rect()

        self.rect.right = self.screen_rect.right
        self.rect.centery = self.screen_rect.centery

        # Store the monster's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the monster at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the monster."""
        pass
