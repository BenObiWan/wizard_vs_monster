#!/usr/bin/env python3
import sys
import pygame
from pygame.sprite import Group

from settings import Settings



def run_game():
    # Initialise
    pygame.init()
    config = Configuration()
    screen = pygame.display.set_mode((config.screen_width, config.screen_height))
    pygame.display.set_caption("Wizard vs Monster")

    # main loop
    #while True:

run_game()
