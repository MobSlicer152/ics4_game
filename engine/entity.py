"""This module implements entities"""

from pygame import Rect, Vector2

from . import camera
from .anim import Animation
from .render import Renderable
from .sprite import Sprite
from .time import get_delta

class Entity(Renderable):
    id = 0

    def __init__(
        self,
        position: Vector2 = Vector2(0),
        sprite: Sprite | Animation | None = None,
        hitbox: Vector2 | None = None,
        allow_collision: bool = True,
        frozen: bool = False,
        name: str | None = None,
    ):
        """Create a new entity"""

        self.name = name
        self.id = Entity.id
        Entity.id += 1

        self.sprite = sprite
        self.hitbox = hitbox
        
        if self.hitbox is None and self.sprite is not None:
            self.hitbox = self.sprite.get_size()
        
        self.position = position
        self.velocity = Vector2(0)
        
        self.allow_collision = allow_collision
        self.frozen = frozen
        
    def draw(self):
        self.sprite.draw(camera.world2screen(self.position, self))
        
    def get_size(self):
        return self.sprite.get_size()
    
    def update(self):
        if not self.frozen:
            self.position += self.velocity * get_delta()
            
        if isinstance(self.sprite, Animation):
            self.sprite.update(get_delta())
