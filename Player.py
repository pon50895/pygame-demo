import pygame
import GlobalParams
from Bullet import Bullet
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GlobalParams.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (GlobalParams.WIDTH / 2, GlobalParams.WIDTH - GlobalParams.BASIC_Y)
        self.lives = 3

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            self.speedx = -1 * GlobalParams.BASIC_SPEED_X
        elif key_pressed[pygame.K_RIGHT]:
            self.speedx = GlobalParams.BASIC_SPEED_X
        else:
            self.speedx = 0

        if key_pressed[pygame.K_UP]:
            self.speedy = -1 * GlobalParams.BASIC_SPEED_Y
        elif key_pressed[pygame.K_DOWN]:
            self.speedy = GlobalParams.BASIC_SPEED_Y
        else:
            self.speedy = 0

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > GlobalParams.WIDTH:
            self.rect.right = GlobalParams.WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > GlobalParams.HEIGHT:
            self.rect.bottom = GlobalParams.HEIGHT

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        return bullet
    def loseLife(self):
        self.lives -= 1