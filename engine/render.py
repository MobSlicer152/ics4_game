"""This module manages an intermediary surface that gets rendered to and then scaled up and copied to the window"""

from typing import *

from pygame import transform
from pygame import Color, Rect, Surface, Vector2

from .level import TILE_SIZE

# The size of the render target
RENDER_TARGET_SIZE = Vector2(TILE_SIZE * 20, TILE_SIZE * 15) # 320 x 240

# The aspect ratio of the render target
RENDER_TARGET_ASPECT = RENDER_TARGET_SIZE.x / RENDER_TARGET_SIZE.y

# The size of the window when it's first created
INITIAL_WINDOW_SIZE = RENDER_TARGET_SIZE * 3 # 960 x 720 is reasonable

# Intermediary surface for drawing to, gets copied to the window every frame
__render_target__: Surface = None


def init():
    """Initializes the renderer"""

    print("Initializing renderer")

    print(f"Creating {RENDER_TARGET_SIZE.x:.0f}x{RENDER_TARGET_SIZE.y:.0f} render target")

    global __render_target__
    __render_target__ = Surface(RENDER_TARGET_SIZE)


def get_render_target() -> Surface:
    """Gets the render target"""
    global __render_target__
    return __render_target__


def begin():
    """Clears the render target"""
    get_render_target().fill(Color(50, 50, 50))


def present(window: Surface):
    """Copies the render target to the window. It gets scaled up while maintaining its aspect ratio, and remaining centered on the screen."""
    
    (width, height) = window.get_size()
    
    # find the smaller dimension of the window
    size = width if width < height else height

    # calculate the biggest size that'll fit in the window with the right aspect ratio
    scale = Vector2(size * RENDER_TARGET_ASPECT, size)
    
    # center it the image
    dest = Vector2(
        width / 2 - scale.x / 2,
        height / 2 - scale.y / 2
    )
    
    # scale the render target and blit it
    scaled = transform.scale(get_render_target(), scale)
    window.blit(scaled, dest)
