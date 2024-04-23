import pygame
import GlobalParams
from Player import Player
from Rock import Rock

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((GlobalParams.WIDTH, GlobalParams.HEIGHT))
pygame.display.set_caption(GlobalParams.GAME_NAME)
clock = pygame.time.Clock()
# TODO load images
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
    bullectCollisions = pygame.sprite.groupcollide(rockGroup, bulletGroup, True, True)
    # check for collisions with rocks and increase score
    if bullectCollisions:
        for bullectCollision in bullectCollisions:
            score += 1
            rock = Rock()
            all_sprites.add(rock)
            rockGroup.add(rock)

    # check for collisions with player
    playerCollisions = pygame.sprite.spritecollide(player, rockGroup, True)
    if playerCollisions:
        player.loseLife()
        if player.lives == 0:
            # game over
            # TODO: pygame.quit()
            pass

    # draw game state
    screen.fill(GlobalParams.BLACK)
    # draw all sprites
    all_sprites.draw(screen)

    # display score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, GlobalParams.WHITE)
    screen.blit(score_text, (10, 10))

    # update display
    pygame.display.flip()
    pygame.display.update()
