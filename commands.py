from entity import Entity
from components import Velocity_Component
from settings import PLAYER_SPEED
import pgzero, pgzrun, pygame
import math, sys, random
class Command:
    def execute(self):
        raise NotImplementedError("Must override execute in subclass")

class MoveBatUpCommand(Command):
    def __init__(self, bat):
        self.bat = bat

    def execute(self):
        velocity = self.bat.get_component(Velocity_Component)
        if velocity is not None:
            velocity.dy = -PLAYER_SPEED

class MoveBatDownCommand(Command):
    def __init__(self, bat):
        self.bat = bat

    def execute(self):
        velocity = self.bat.get_component(Velocity_Component)
        if velocity is not None:
            velocity.dy = PLAYER_SPEED