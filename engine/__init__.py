"""This module has core functions and definitions for the engine package"""

import pygame

from pygame import Color

from . import render

__all__ = ["anim", "collision", "entity", "input", "level", "render", "sprite", "ui"]

def init():
    """Initializes the engine"""

    print("Initializing engine")

    print("Initializing pygame")
    pygame.init()

    render.init()


def process_events() -> bool:
    """Processes events, returns False if the engine is no longer running"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
    return True


def run(game_name: str):
    """Main loop for the whole program"""

    print(f"Creating {render.INITIAL_WINDOW_SIZE.x:.0f}x{render.INITIAL_WINDOW_SIZE.y:.0f} window titled \"{game_name}\"")
    pygame.display.set_caption(game_name)
    window = pygame.display.set_mode(render.INITIAL_WINDOW_SIZE, pygame.RESIZABLE)

    running = True
    while running:
        running = process_events()

        window.fill(Color(0, 0, 0))

        render.begin()

        

        render.present(window)

        pygame.display.flip()
