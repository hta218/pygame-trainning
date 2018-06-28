import pygame
from game_object import GameObject
BLUE = (0, 0, 255)


class BoxCollider(GameObject):
    def __init__(self, width, height):
        GameObject.__init__(self, 0, 0)
        # self.x = x
        # self.y = y
        self.width = width
        self.height = height

    def corners(self):
        return (
            self.x - self.width / 2,
            self.x + self.width / 2,
            self.y - self.height / 2,
            self.y + self.height / 2,
            )

    def collide_with(self, other):
        left1, right1, top1, bottom1 = self.corners()
        left2, right2, top2, bottom2 = other.corners()

        x_overlap = right2 >= left1 and left2 <= right1
        y_overlap = top2 <= bottom1 and bottom2 >= top1

        return x_overlap and y_overlap

    def render(self, canvas):
        rect = (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)
        pygame.draw.rect(canvas, BLUE, rect, 1)


# box1 = BoxCollider(10, 20, 30, 30)
# box2 = BoxCollider(20, 20, 30, 30)
#
# print(box1.collide_with(box2))