#!/usr/bin/env python3
import sys
import pygame
from pygame.sprite import Group

from settings import Settings



def run_game():
    # Initialise
    pygame.init()
    game_settings=Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Wizard vs Monster")

    # main loop
    #while True:

run_game()
