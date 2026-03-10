import random
from pgzero.builtins import Actor, keyboard
from pgzhelper import *

class Knight(Actor):
    def __init__(self):
        super().__init__('run1')
        self.x = 100
        self.y = 470
        self.images = ['run1', 'run2', 'run3', 'run4', 'run5', 'run6', 'run7', 'run8', 'run9', 'run10']
        self.fps = 15
        
        self.velocity = 0
        self.gravity = 0.5
        self.ground_level = 470

    def move(self):
        self.animate() # from pgzhelper

        if keyboard.up and self.y == self.ground_level:
            self.velocity = -20
            
        self.y += self.velocity
        self.velocity += self.gravity

        if self.y >= self.ground_level:
            self.velocity = 0
            self.y = self.ground_level


class Bat(Actor):
    def __init__(self):
        super().__init__('bat1')
        self.images = ['bat1', 'bat2', 'bat3', 'bat4']
        self.fps = 10
        self.reset_position() 

    def reset_position(self):
        self.x = random.randint(900, 2000)
        self.y = random.randint(100, 250)

    def move(self):
        self.animate()
        self.x -= 5
        if self.x < -50:
            self.reset_position()


class Enemy(Actor):
    def __init__(self):
        super().__init__('pokermad')
        self.x = 860
        self.y = 500
        self.speed = 8

    def move(self):
        self.x -= self.speed