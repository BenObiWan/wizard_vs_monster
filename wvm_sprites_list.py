from pygame.sprite import Group
from wizard import Wizard

class WvmSpritesList():
    """A class listing all the Sprites of the game."""

    def __init__(self, config, screen):
        """Initialize the sprite list."""
        self.config = config
        self.screen = screen

        #initialize the sprites
        self.wiz = Wizard(config, self)
        self.monsters = Group()
        self.missiles = Group()

    def update_all(self):
        """Update the positions of all sprites."""
        self.wiz.update()

    def draw(self):
        self.screen.fill(self.config.bg_color)
        self.wiz.blitme()
