import pygame
from game_object import GameObject
from physic.box_collider import BoxCollider

class Enemy(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("images/enemy/bacteria1.png")
        self.box_collider = BoxCollider(30, 30)


    def update(self):
        GameObject.update(self)
        self.deactivate_if_needed()
        self.y += 3

    def deactivate_if_needed(self):
        if self.y > 800:
            self.deactivate()