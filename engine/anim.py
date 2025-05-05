"""This module implements classes for animated sprites"""

import pygame

from pygame import Surface, Vector2

from engine import render
from engine.render import Renderable
from engine.sprite import Sprite, SpriteSheet


class Animation(Renderable):
    """Keeps track of the current frame of a sprite sheet animation"""

    def __init__(self, frames: SpriteSheet, frame_time: float = 0.016):
        self.frames = frames
        self.frame_time = frame_time
        self.frame_size = self.frames.sprite_size

        self._frame = 0
        self._timer = 0

    def update(self, delta: float):
        """Advances the timer by the delta given, possibly updating what the current frame is"""
        self._timer += delta
        if self._timer >= self.frame_time:
            self._timer = 0
            self._frame = (self._frame + 1) % len(self.frames)
    
    def get_frame(self) -> Sprite:
        """Returns the current frame"""
        return Sprite(self.frames, self._frame)
    
    def draw(self, where: Vector2):
        self.get_frame().draw(where)
        
    def get_size(self) -> Vector2:
        return self.frame_size
