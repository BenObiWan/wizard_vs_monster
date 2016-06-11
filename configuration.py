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

        self.initialize_dynamic_configurations()

    def initialize_dynamic_configurations(self):
        """Initialize configurations that change throughout the game."""
        pass
