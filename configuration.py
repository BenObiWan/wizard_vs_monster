class Configuration():
    """A class to store configuration."""

    def __init__(self):
        """Initialize the game's static configuration."""
        # Screen configurations
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Wizard configurations
        self.init_life = 3
        self.wizard_speed_factor = 1.5

        # Starting magic missile settings
        self.start_magic_missile_width = 15
        self.start_magic_missile_heigth = 3
        self.start_magic_missile_color = 60, 60, 60
        self.start_magic_missile_allowed = 3
        self.start_magic_missile_speed_factor = 3

