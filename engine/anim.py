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

        self.__frame__ = 0
        self.__timer__ = 0

    def update(self, delta: float):
        """Advances the timer by the delta given, possibly updating what the current frame is"""
        self.__timer__ += delta
        if self.__timer__ >= self.frame_time:
            self.__timer__ = 0
            self.__frame__ = (self.__frame__ + 1) % len(self.frames)
    
    def get_frame(self) -> Sprite:
        """Returns the current frame"""
        return Sprite(self.frames, self.__frame__)
    
    def draw(self, where: Vector2):
        self.get_frame().draw(where)
        
    def get_size(self) -> Vector2:
        return self.frame_size
