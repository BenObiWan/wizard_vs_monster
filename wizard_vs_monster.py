#!/usr/bin/env python3
import sys
import pygame
from pygame.sprite import Group

from configuration import Configuration
from wvm_sprites_list import WvmSpritesList

import game_functions as gf

def run_game():
    # Initialise
    pygame.init()
    config = Configuration()
    screen = pygame.display.set_mode((config.screen_width, config.screen_height))
    pygame.display.set_caption("Wizard vs Monster")
    sprites_list = WvmSpritesList(config, screen)

    # main loop
    while True:
        gf.check_events(config, sprites_list)
        sprites_list.update_all()
        gf.update_screen(config, sprites_list)

run_game()
