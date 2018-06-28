import pygame
from player.player import Player
from enemy.enemy import Enemy
from enemy.enemy_spawner import EnemySpawner
from input.input_manager import InputManager
import game_object


BG = (125, 60, 60)

# 1. Init pygame
pygame.init()

# 2. Set up screen
size = (600, 800)
canvas = pygame.display.set_mode(size)

# 5. Clock
clock = pygame.time.Clock()

# 4. Load image
# player_img = pygame.image.load('images/player/player1.png')
# player_x = 100
# player_y = 100

# 9. Input manager
input_manager = InputManager()

# 8. Create player
enemy = Enemy(400, 100)
player = Player(100, 100, input_manager)
enemy_spawner = EnemySpawner()


# 14. Game object (Addition)
game_object.add(player)
# game_object.add(enemy)
game_object.add(enemy_spawner)


# 3. Create gameloop
loop = True
while loop:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            input_manager.update(event)

    # 14. game object
    game_object.update()

    canvas.fill(BG)

    # 14. game object
    game_object.render(canvas)

    clock.tick(60)
    pygame.display.flip()
