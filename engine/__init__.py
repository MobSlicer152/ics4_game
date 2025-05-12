"""This module has core functions and definitions for the engine package"""

import pygame

from pygame import Color, Vector2, draw, mouse
from pygame.time import Clock

from engine.anim import Animation
from engine.sprite import SpriteSheet

from . import input, render, settings
from engine import camera

__all__ = ["anim", "collision", "entity", "input", "level", "render", "settings", "sprite", "ui"]

# engine clock
_clock = Clock()

def init():
    """Initializes the engine"""

    print("Initializing engine")

    print("Initializing pygame")
    pygame.init()

    render.init()
    settings.init()


def process_events() -> bool:
    """Processes events, returns False if the engine is no longer running"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

    return True


def get_delta() -> float:
    """Gets the time since the last frame in seconds"""
    global _clock
    return _clock.get_time() / 1000.0


def run(game_name: str):
    """Main loop for the whole program"""

    print(f"Creating {render.INITIAL_WINDOW_SIZE.x:.0f}x{render.INITIAL_WINDOW_SIZE.y:.0f} window titled \"{game_name}\"")
    pygame.display.set_caption(game_name)
    window = pygame.display.set_mode(render.INITIAL_WINDOW_SIZE, pygame.RESIZABLE)

    test_sheet = SpriteSheet("animtest.png")
    test_anim = Animation(test_sheet, 0.05)

    global _clock

    running = True
    while running:
        running = process_events()

        window.fill(Color(0, 0, 0))

        render.begin()

        input.update()

        offset = input.get_left_axis()
        offset.x *= test_anim.frame_size.x
        offset.y *= -test_anim.frame_size.y

        camera.move(offset)

        cursor_pos = input.get_cursor()
        draw.line(render.get_render_target(), Color(255, 0, 0), camera.world2screen(Vector2(0)), cursor_pos)
        draw.circle(render.get_render_target(), Color(255, 0, 0), cursor_pos, 5)

        render.present(window)

        _clock.tick(60)

        pygame.display.flip()
