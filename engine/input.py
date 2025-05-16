"""This module implements functions for user input and controls"""

import pygame

from pygame import Vector2
from pygame import display, event, key, mouse

from . import camera, settings

# whether the current input is a controller (TODO: implement controller support when stuff is done)
_is_controller = False

# wasd, arrow keys, or left joystick
# TODO: allow rebinding keys?
_left_axis = Vector2(0)
# mouse or right joystick
_cursor = Vector2(0)

# buttons are <xbox>/<playstation>
# bit 0 is x/square, bit 1 is y/triangle, bit 2 is b/circle, bit 3 is a/cross
# keyboard mappings tbd
_buttons: int = 0
_BUTTON_X_MASK = 0b0001
_BUTTON_Y_MASK = 0b0010
_BUTTON_B_MASK = 0b0100
_BUTTON_A_MASK = 0b1000

def init():
    """Registers settings for the input system"""
    settings.add("sensitivity", 0.2, float)


def update():
    """Updates the current input state"""

    global _is_controller
    global _left_axis
    global _cursor
    global _buttons

    _left_axis = Vector2(0, 0)

    _buttons = 0

    # check controller stuff
    if _is_controller:
        pass
    else:
        keyboard = key.get_pressed()

        # add and subtract so one key doesn't override the other
        if keyboard[pygame.K_w] or keyboard[pygame.K_UP]:
            _left_axis.y -= 1
        if keyboard[pygame.K_s] or keyboard[pygame.K_DOWN]:
            _left_axis.y += 1
        if keyboard[pygame.K_a] or keyboard[pygame.K_LEFT]:
            _left_axis.x -= 1
        if keyboard[pygame.K_d] or keyboard[pygame.K_RIGHT]:
            _left_axis.x += 1

        if _left_axis.length() > 0:
            _left_axis = _left_axis.normalize()

        (w, h) = display.get_window_size()
        mouse.set_pos((w / 2, h / 2))
        mouse.set_visible(False)
        event.set_grab(True)

        mouse_rel = Vector2(mouse.get_rel())
        _cursor += mouse_rel * settings.get("sensitivity")


def get_left_axis() -> Vector2:
    global _left_axis
    return _left_axis


def get_cursor() -> Vector2:
    global _cursor
    return _cursor


def get_x() -> bool:
    global _buttons
    return bool(_buttons & _BUTTON_X_MASK)


def get_y() -> bool:
    global _buttons
    return bool(_buttons & _BUTTON_Y_MASK)


def get_b() -> bool:
    global _buttons
    return bool(_buttons & _BUTTON_B_MASK)


def get_a() -> bool:
    global _buttons
    return bool(_buttons & _BUTTON_A_MASK)
