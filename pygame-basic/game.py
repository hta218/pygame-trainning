import pygame

WHITE = (255, 255, 255)

# 1. Init pygame
pygame.init()

# 2. Set up screen
size = (600, 800)
canvas = pygame.display.set_mode(size)

# 5. Clock
# clock = pygame.time.Clock()

# 4. Load image
player_img = pygame.image.load('player1.png')
player_x = 100
player_y = 100


# 3. Create gameloop
loop = True
while loop:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x += 10

    canvas.fill(WHITE)
    canvas.blit(player_img, (player_x, player_y))

    # clock.tick(60)
    pygame.display.flip()
