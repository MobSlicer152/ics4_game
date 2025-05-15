"""This module has core functions and definitions for the engine package"""

import pygame

from pygame import Color, Vector2, draw, mouse

from .anim import Animation
from .entity import Entity
from .sprite import SpriteSheet

from . import camera, input, render, settings, time

__all__ = ["anim", "collision", "entity", "input", "level", "render", "settings", "sprite", "time", "ui"]

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


def run(game_name: str):
    """Main loop for the whole program"""

    print(f"Creating {render.INITIAL_WINDOW_SIZE.x:.0f}x{render.INITIAL_WINDOW_SIZE.y:.0f} window titled \"{game_name}\"")
    pygame.display.set_caption(game_name)
    window = pygame.display.set_mode(render.INITIAL_WINDOW_SIZE, pygame.RESIZABLE)

    test_sheet = SpriteSheet("animtest.png")
    test_anim = Animation(test_sheet, 0.05)
    player = Entity(sprite=test_anim)

    running = True
    while running:
        running = process_events()

        window.fill(Color(0, 0, 0))

        render.begin(Color(50, 50, 50))

        input.update()
        
        player.velocity = input.get_left_axis() * 10
        
        player.update()
        player.draw()

        cursor_pos = input.get_cursor()
        draw.line(render.get_render_target(), Color(255, 0, 0), camera.world2screen(player.position, player), cursor_pos)
        draw.circle(render.get_render_target(), Color(255, 0, 0), cursor_pos, 5)

        render.present(window)

        time.tick(60)

        pygame.display.flip()
