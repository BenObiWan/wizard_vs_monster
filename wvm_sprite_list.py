from pygame.sprite import Group
from wizard import Wizard

class WvmSpriteList():
    """A class listing all the Sprites of the game."""

    def __init__(self, config):
        """Initialize the sprite list."""
        self.config = config
        self.wiz = Wizard(config)
        self.monsters = Group()
        self.missiles = Group()

