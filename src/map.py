import pygame
from player import Player

class Map():
    def __init__(self):
        self.player = [Player()]
        self.ground = []
        self.rect = pygame.Rect(0,0,0,0)
        self.GREEN = (0,255,0)

    def add_ground(self, display, mouse_pos):
        self.ground.append(mouse_pos)
        print(self.ground)

    def draw(self, display):
        pygame.draw.polygon(display, self.GREEN, self.ground)

    def draw(self, display, positions):
        pygame.draw.rect(display, self.GREEN, positions)
        self.rect = pygame.Rect((200,600), (400, 0))

    def check_landed(self, rect1, rect2, displayLength):
        if(self.doOverlap(rect1.topleft, rect1.bottomright, rect2.topleft,rect2.bottomright)):
            print("landed")
            for j in range(len(self.player)):
                self.player[j].vertical_movement(0,displayLength)
                self.player[j].acceleration.y = 0
                self.player[j].gravity = 0

    def doOverlap(self, l1, r1, l2, r2): 
        # If one rectangle is on left side of other 
        print("vertical " + str(l1[1] <= r2[1] or l2[1] <= r1[1]))
        if(l1[0] >= r2[0] or l2[0] >= r1[0]): 
            return False
        # If one rectangle is above other 
        if(l1[1] <= r2[1] or l2[1] <= r1[1]): 
            return False
        return True