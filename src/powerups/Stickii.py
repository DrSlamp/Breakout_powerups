"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the specialization of PowerUp to add two more ball to the game.
"""

"""
Pol
"""
import numpy as np
from numpy import random
import random
import pygame
from typing import TypeVar

from gale.factory import Factory

import settings
from src.Ball import Ball
from src.Paddle import Paddle
from src.powerups.PowerUp import PowerUp



class Stickii(PowerUp):
    """
    Power-up to add two more ball to the game.
    """

    
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 8)
        self.ball_factory = Factory(Ball)
        self.paddle_factory = Factory(Paddle)

       







    def take(self, play_state: TypeVar("PlayState")) -> None:
        paddle = play_state.paddle


    #pendiente para continuar...
        def __init__(self, x: int, y: int) -> None:
            super().__init__(x, y, 8)
            self.x = x
            self.y = y
        self.width = 64
        self.height = 16

        # By default, the blue paddle
        self.skin = np.random.randint(0,3)

        # By default, the 64-pixels-width paddle.
        self.size = np.random.randint(0,3)

        self.texture = settings.TEXTURES["spritesheet"]
        self.frames = settings.FRAMES["paddles"]

       

        def render(self, surface: pygame.Surface) -> None:
            surface.blit(self.texture, (self.x, self.y), self.frames[self.skin][self.size])



        for _ in range(5):
            b = self.ball_factory.create(paddle.x + paddle.width // 2 - 4, paddle.y - 8)
            settings.SOUNDS["paddle_hit"].stop()
            settings.SOUNDS["paddle_hit"].play()    


        

        b.x = 0 
        b.y = 0
    
        #play_state.balls.append(b)



        



        self.in_play = False
