import pygame
import GlobalParams


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((GlobalParams.BULLET_WIDTH, GlobalParams.BULLET_HEIGHT))
        self.image.fill(GlobalParams.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedy = -1 * GlobalParams.BULLET_SPEED

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0 or self.rect.right < 0 or self.rect.left > GlobalParams.WIDTH:
            self.kill()
