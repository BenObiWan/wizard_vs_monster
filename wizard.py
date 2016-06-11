import pygame
from pygame.sprite import Sprite

class Wizard(Sprite):
    """A class representing the Wizard"""

    def __init__(self, config):
        """Initialize the wizard."""
        super().__init__()
        self.config = config
