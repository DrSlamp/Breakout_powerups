"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the specialization of PowerUp to add two more ball to the game.
"""
import random
import pygame
import time
from typing import TypeVar

from gale.factory import Factory

import settings
#from src.Ball import Ball
from src.BallRainb import BallR
from src.powerups.PowerUp_Rain import PowerUp_Rain
from gale.text import render_text
from gale.factory import AbstractFactory



class BallRain(PowerUp_Rain):
    """
    Power-up to add little waterdrops to the game.
    """
    """
    def render(self, surface: pygame.Surface) -> None:
                 
                 render_text(
            surface,
           
            f"RAINTIME",
            settings.FONTS["tiny"],
            settings.VIRTUAL_WIDTH - 195,
            5,
            (0, 168, 243),
            
           
        )
    """
     

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 8)
        self.ball_factory = Factory(BallR)

    

    def take(self, play_state: TypeVar("PlayState")) -> None:
        paddle = play_state.paddle
        
 
        for _ in range(2):
            s = self.ball_factory.create(paddle.x + paddle.width  - 4, 0)
            settings.SOUNDS["paddle_hit"].stop()
            settings.SOUNDS["paddle_hit"].play()
            

            s.vx = random.randint(-170, -100)
            s.vy = paddle.y + paddle.width  - 2
            
            play_state.balls.append(s)

          

        self.in_play = False
        

    
        

   