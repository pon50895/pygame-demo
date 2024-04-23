import pygame
import GlobalParams
from Player import Player
from Rock import Rock

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((GlobalParams.WIDTH, GlobalParams.HEIGHT))
pygame.display.set_caption(GlobalParams.GAME_NAME)
clock = pygame.time.Clock()
score = 0

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
rockGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()

# Generate rocks
for i in range(GlobalParams.MAX_ROCKS):
    rock = Rock()
    all_sprites.add(rock)
    rockGroup.add(rock)


# Game loop
while True:
    # set FPS
    clock.tick(GlobalParams.FPS_FRAME)
    # get input from user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = player.shoot()
                all_sprites.add(bullet)
                bulletGroup.add(bullet)

    # update game state
    all_sprites.update()
    collisions = pygame.sprite.groupcollide(rockGroup, bulletGroup, True, True)
    # check for collisions with rocks and increase score
    if collisions:
        for collision in collisions:
            score += 1
            rock = Rock()
            all_sprites.add(rock)
            rockGroup.add(rock)

    # draw game state
    screen.fill(GlobalParams.BLACK)
    # draw all sprites
    all_sprites.draw(screen)

    # update display
    pygame.display.update()
