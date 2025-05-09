"""This module implements the camera system, which turns absolute positions/sizes into screen positions/sizes"""

import pygame

from pygame import Vector2

from .render import Renderable, RENDER_TARGET_SIZE

# current camera position
_camera_pos = Vector2(0, 0)


def set_pos(pos: Vector2):
    """set the camera's position"""
    global _camera_pos
    _camera_pos = pos


def get_pos(pos: Vector2):
    """get the camera's position"""
    global _camera_pos
    return _camera_pos


def world2screen(pos: Vector2, obj: Renderable | None) -> Vector2:
    """projects a world space position into screen space"""

    global _camera_pos

    center = Vector2(0, 0)
    if obj is not None:
        size = obj.get_size()
        center = Vector2(size.x / 2, size.y / 2)

    # make the camera the origin
    camera = Vector2(pos.x - _camera_pos.x - center.x, pos.y - _camera_pos.y + center.y)

    # convert origin from center to top left
    # https://math.stackexchange.com/questions/1896656/how-do-i-convert-coordinates-from-bottom-left-as-0-0-to-middle-as-0-0
    return Vector2(
        (camera.x + RENDER_TARGET_SIZE.x) / 2, (camera.y + RENDER_TARGET_SIZE.y) / 2
    )


def screen2world(pos: Vector2) -> Vector2:
    """un-projects a screen position into world space"""
    
    global _camera_pos
    return Vector2((pos.x * 2 - RENDER_TARGET_SIZE.x / 2))
