"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the specialization of PowerUp to add pairs of misils.
"""
import random
import pygame
import time
from typing import TypeVar

from gale.factory import Factory

import settings
#from src.Ball import Ball
from src.Misil import Misil


from src.powerups.PowerUp_cannon import PowerUp_Cannon
from gale.text import render_text
from gale.factory import AbstractFactory


class Missiles(PowerUp_Cannon):
    """
    Power-up to pair of Missiles. 
    Paul B.
    """
             
    

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 8)
        self.ball_factory_misil = Factory(Misil)
        

    def take(self, play_state: TypeVar("PlayState")) -> None:
        paddle = play_state.paddle
        
       
        for _ in range(1):
            b = self.ball_factory_misil.create(paddle.x + 2 , paddle.y)
            c = self.ball_factory_misil.create(paddle.x + 60, paddle.y)
            settings.SOUNDS["paddle_hit"].stop()
            settings.SOUNDS["paddle_hit"].play()

            dt: float 

            dt = 0

            

            b.vx = random.randint(-170, -100) * dt
            b.vy = - paddle.y - paddle.width  - 2
            play_state.balls.append(b)

            c.vx = random.randint(-170, -100) * dt
            c.vy = - paddle.y - paddle.width  - 2
            play_state.balls.append(c)


        self.in_play = False

    
        