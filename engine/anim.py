import pygame

from pygame import Surface, Vector2
from sprite import SpriteSheet

class Animation:
	"""Keeps track of the current frame of a sprite sheet animation"""

	__frame__: int  # The current frame
	__timer__: int  # The timer

	def __init__(self, frames: SpriteSheet, frame_time: float = 0.016):
		self.frames = frames
		self.frame_time = frame_time
		self.frame_size = self.frames.sprite_size

		self.__frame__ = 0
		self.__timer__ = 0

	def frame(self, delta_millis: int) -> Surface:
		"""Returns the current frame of the animation after advancing the timer by the delta given"""
		self.__timer__ += delta_millis
		if self.__timer__ / 1000 >= self.frame_time:
			self.__timer__ = 0
			self.__frame__ = (self.__frame__ + 1) % len(self.frames)

		return self.frames[self.__frame__]