from typing import TypeVar, Any

import pygame

import settings

class PowerUp_Rain:
    """
    The base power-up.
    """

    def __init__(self, x: int, y: int, frame: int) -> None:
        self.x = x
        self.y = y
        self.vy = settings.POWERUP_SPEED
        self.in_play = True
        self.frame = frame

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, 16, 16)

    def collides(self, obj: Any) -> bool:
        return self.get_collision_rect().colliderect(obj.get_collision_rect())

    def update(self, dt: float) -> None:
        if self.y > settings.VIRTUAL_HEIGHT:
            self.in_play = False

        self.y += self.vy * dt

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(
            settings.TEXTURES["spritesheet"],
            (self.x, self.y),
            settings.FRAMES["powerups"][self.frame-2],
        )

    def take(self, play_state: TypeVar("PlayState")) -> None:
        raise NotImplementedError