import pygame
import game_object
from game_object import GameObject
from player.player_bullet import PlayerBullet
from frame_counter import FrameCounter


class Player(GameObject):
    def __init__(self, x, y, input_manager):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("images/player/player1.png")
        self.input_manager = input_manager
        self.shoot_lock = False
        self.counter = FrameCounter(20)

    def update(self):
        dx = 0
        dy = 0
        step = 5

        if self.input_manager.up_pressed:
            dy -= step
        if self.input_manager.down_pressed:
            dy += step
        if self.input_manager.left_pressed:
            dx -= step
        if self.input_manager.right_pressed:
            dx += step

        self.x += dx
        self.y += dy
        self.shoot()

    def shoot(self):
        if self.input_manager.x_pressed and not self.shoot_lock:
            game_object.recycle(PlayerBullet, self.x, self.y - 15)
            self.shoot_lock = True

        if self.shoot_lock:
            self.counter.run()
            if self.counter.expired:
                self.shoot_lock = False
                self.counter.reset()