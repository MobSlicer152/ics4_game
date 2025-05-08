"""This module implements functions for user input and controls"""

import pygame

from pygame import Vector2
from pygame import key, mouse

_is_controller = False

# wasd, arrow keys, or left joystick
# TODO: allow rebinding keys?
_left_axis: Vector2
# mouse or right joystick
_right_axis: Vector2

# buttons are <xbox>/<playstation>
# bit 0 is x/square, bit 1 is y/triangle, bit 2 is b/circle, bit 3 is a/cross
# keyboard mappings tbd
_buttons: int = 0
_BUTTON_X_MASK = 0b0001
_BUTTON_Y_MASK = 0b0010
_BUTTON_B_MASK = 0b0100
_BUTTON_A_MASK = 0b1000

def update():
    """Updates the current input state"""

    global _is_controller
    global _left_axis
    global _right_axis
    global _buttons

    _left_axis = Vector2(0, 0)
    _right_axis = Vector2(0, 0)

    _buttons = 0

    # check controller stuff
    if _is_controller:
        pass
    else:
        keyboard = key.get_pressed()

        # add and subtract so one key doesn't override the other
        if keyboard[pygame.K_w] or keyboard[pygame.K_UP]:
            _left_axis.y += 1
        if keyboard[pygame.K_s] or keyboard[pygame.K_DOWN]:
            _left_axis.y -= 1
        if keyboard[pygame.K_a] or keyboard[pygame.K_LEFT]:
            _left_axis.x -= 1
        if keyboard[pygame.K_d] or keyboard[pygame.K_RIGHT]:
            _left_axis.x += 1

        # TODO: get the mouse position relative to the center of the screen, needs camera


def get_left_axis() -> Vector2:
    global _left_axis
    return _left_axis


def get_right_axis() -> Vector2:
    global _right_axis
    return _right_axis


def get_x() -> bool:
    global _buttons
    return _buttons & _BUTTON_X_MASK


def get_y() -> bool:
    global _buttons
    return _buttons & _BUTTON_Y_MASK


def get_b() -> bool:
    global _buttons
    return _buttons & _BUTTON_B_MASK


def get_a() -> bool:
    global _buttons
    return _buttons & _BUTTON_A_MASK
