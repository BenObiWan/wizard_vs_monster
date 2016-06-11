import pygame
from pygame.sprite import Sprite

class Monster(Sprite):
    """A class to represent a monster."""

    def __init__(self, config):
        """Initialize the monster and set its starting position."""
        super().__init__()
        self.config = config

