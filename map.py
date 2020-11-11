import pygame
from player import Player

class Map():
    def __init__(self):
        self.player = Player()
        self.ground = []
        self.GREEN = (0,255,0)

    def add_ground(self, display, mouse_pos):
        self.ground.append(mouse_pos)
        print(self.ground)
    def draw(self, display):
        pygame.draw.polygon(display, self.GREEN, self.ground)