"""This module implements sprites and sprite sheets"""

from typing import AnyStr, Union

import pygame

from pygame import Rect, Surface, Vector2

from engine import render
from engine.render import Renderable


class Sprite(Renderable):
    """A reference to a sprite in a sprite sheet"""

    def __init__(self, sheet: "SpriteSheet", index: int):
        self.sheet = sheet
        self.index = index

    def get(self) -> Surface:
        return self.sheet[self.index]

    def draw(self, where: Vector2):
        render.draw(self.get(), where - self.get_size() / 2)

    def get_size(self) -> Vector2:
        return self.sheet.sprite_size


class SpriteSheet:
    """Allows for dividing up images into multiple sprites"""

    def __init__(
        self,
        image: Union[AnyStr, Surface],
        sprite_count: int = 0,
        sprite_size: Vector2 = Vector2(16, 16),
        distance: int = 0,
        vertical: bool = False,
        offset_pos: Vector2 = Vector2(0, 0),
    ):
        # Either use a surface from an already loaded image, or load a file
        if type(image) == str:
            self.image = pygame.image.load(image)
        else:
            self.image = image

        # Apply an offset if there is one by copying from the offset to the bottom right corner of the image
        if offset_pos != (0, 0):
            tmp = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
            tmp.blit(
                self.image,
                (0, 0),
                pygame.Rect(
                    offset_pos[0],
                    offset_pos[1],
                    self.image.get_width() - offset_pos[0],
                    self.image.get_height() - offset_pos[1],
                ),
            )
            self.image = tmp
        self.sprite_size = sprite_size
        self.distance = distance
        self.vertical = vertical

        # If the sprite count is 0, calculate it automatically
        if sprite_count == 0:
            if self.vertical:
                self.sprite_count = self.image.get_height() // (
                    self.sprite_size[1] + self.distance
                )
            else:
                self.sprite_count = self.image.get_width() // (
                    self.sprite_size[0] + self.distance
                )
        else:
            self.sprite_count = sprite_count
        self.sprite_count = int(self.sprite_count)

    def __getitem__(self, key: int) -> Sprite:
        sprite = pygame.Surface(self.sprite_size, pygame.SRCALPHA)

        if self.vertical:
            area = pygame.Rect(
                0,
                (self.sprite_size[1] + self.distance) * key,
                self.sprite_size[0],
                self.sprite_size[1],
            )
        else:
            area = pygame.Rect(
                (self.sprite_size[1] + self.distance) * key,
                0,
                self.sprite_size[0],
                self.sprite_size[1],
            )

        sprite.blit(self.image, (0, 0), area)
        return sprite

    def __len__(self):
        return self.sprite_count
