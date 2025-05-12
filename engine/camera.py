"""This module implements the camera system, which turns absolute positions/sizes into screen positions/sizes"""

from pygame import Vector2
from pygame.display import get_window_size

from .render import Renderable, RENDER_TARGET_SIZE

# current camera position
_camera_pos = Vector2(0, 0)


def move(change: Vector2):
    """move the camera"""
    global _camera_pos
    _camera_pos += change


def set_pos(pos: Vector2):
    """set the camera's position"""
    global _camera_pos
    _camera_pos = pos


def get_pos():
    """get the camera's position"""
    global _camera_pos
    return _camera_pos


def world2screen(pos: Vector2, obj: Renderable | None = None) -> Vector2:
    """projects a world space position into screen space"""

    global _camera_pos

    center = Vector2(0, 0)
    if obj is not None:
        size = obj.get_size()
        center = Vector2(size.x / 2, size.y / 2)

    # make the camera the origin
    camera = Vector2((pos.x - _camera_pos.x) - center.x, (pos.y - _camera_pos.y) + center.y)

    # convert origin from center to top left
    # https://math.stackexchange.com/questions/1896656/how-do-i-convert-coordinates-from-bottom-left-as-0-0-to-middle-as-0-0
    return Vector2(
        (camera.x + RENDER_TARGET_SIZE.x) / 2, (camera.y + RENDER_TARGET_SIZE.y) / 2
    )


def screen2world(pos: Vector2) -> Vector2:
    """un-projects a screen position into world space"""

    global _camera_pos
    # https://github.com/MobSlicer152/ld55/blob/main/game/systems/input.c#L14
    #
    (width, height) = get_window_size()
    # change origin to center from top left
    centered = Vector2(pos.x - width / 2, pos.y - height / 2)
    # scale to render target space
    screen = Vector2(centered.x / width * RENDER_TARGET_SIZE.x, centered.y / height * RENDER_TARGET_SIZE.y)
    return screen
