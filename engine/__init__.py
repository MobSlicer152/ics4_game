"""This module has core functions and definitions for the engine package"""

import pygame

from pygame import Color
from pygame.time import Clock

from engine.anim import Animation
from engine.sprite import SpriteSheet

from . import render

__all__ = ["anim", "collision", "entity", "input", "level", "render", "sprite", "ui"]

# engine clock
__clock__ = Clock()

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


def get_delta() -> float:
    """Gets the time since the last frame in seconds"""
    global __clock__
    return __clock__.get_time() / 1000.0


def run(game_name: str):
    """Main loop for the whole program"""

    print(f"Creating {render.INITIAL_WINDOW_SIZE.x:.0f}x{render.INITIAL_WINDOW_SIZE.y:.0f} window titled \"{game_name}\"")
    pygame.display.set_caption(game_name)
    window = pygame.display.set_mode(render.INITIAL_WINDOW_SIZE, pygame.RESIZABLE)

    test_sheet = SpriteSheet("animtest.png", sprite_size=(128, 128))
    test_anim = Animation(test_sheet, 0.05)
    
    global __clock__

    running = True
    while running:
        running = process_events()

        window.fill(Color(0, 0, 0))

        render.begin()

        test_anim.update(get_delta())
        for y in range(0, int(render.RENDER_TARGET_SIZE.y), 128):
            for x in range(0, int(render.RENDER_TARGET_SIZE.y), 128):
                test_anim.draw((x, y))

        render.present(window)

        __clock__.tick(60)

        pygame.display.flip()
