from pygame.sprite import Group
from wizard import Wizard
from magic_missile import MagicMissile
from monster import Monster

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
        self.update_missiles()
        self.wiz.update()
        self.monsters.update()

    def update_missiles(self):
        """update magic missiles positions"""
        self.missiles.update()
        # remove the missiles that have left the screen
        for mi in self.missiles.copy():
            if mi.rect.left >= self.screen.get_rect().right:
                self.missiles.remove(mi)

    def draw(self):
        self.screen.fill(self.config.bg_color)
        for mi in self.missiles:
            mi.draw_missile()
        self.wiz.blitme()
        for mo in self.monsters:
            mo.blitme()

    def fire_missile(self):
        """Fire a missile if limit not reached yet."""
        if len(self.missiles) < self.wiz.magic_missile_allowed:
            self.missiles.add(MagicMissile(self.config, self))

    def create_monster(self):
        """Create a new monster and place it randomly at the right."""
        monster=Monster(self.config, self)
        #TODO move the monster
        self.monsters.add(monster)
