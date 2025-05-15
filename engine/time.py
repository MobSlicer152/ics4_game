"""This module handles time"""

from pygame.time import Clock

# engine clock
_clock = Clock()


def tick(fps: float):
    """Ticks the clock"""
    global _clock
    _clock.tick(fps)


def get_delta() -> float:
    """Gets the time since the last frame in seconds"""
    global _clock
    return _clock.get_time() / 1000.0
