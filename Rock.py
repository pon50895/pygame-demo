import pygame
import GlobalParams
import random

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((GlobalParams.ROCK_WIDTH, GlobalParams.ROCK_HEIGHT))
        self.image.fill(GlobalParams.RED)
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randrange(0, GlobalParams.WIDTH - GlobalParams.ROCK_WIDTH / 2),
            -GlobalParams.ROCK_HEIGHT / 2
        )
        self.speedx = random.randrange(-GlobalParams.ROCK_SPEED_X_COEFFICIENT, GlobalParams.ROCK_SPEED_X_COEFFICIENT)
        self.speedy = GlobalParams.ROCK_SPEED_Y

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > GlobalParams.WIDTH or self.rect.right < 0 or self.rect.left > GlobalParams.WIDTH:
            self.rect.center = (
                random.randrange(0, GlobalParams.WIDTH - GlobalParams.ROCK_WIDTH / 2),
                -GlobalParams.ROCK_HEIGHT / 2
            )
