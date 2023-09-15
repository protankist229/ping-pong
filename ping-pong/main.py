import pygame
import random

pygame.init()
window = pygame.display.set_mode((600, 500))

window.fill((200, 255, 255))
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

    def update_2(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

racket_left = Player('racket.png', 30, 200, 4, 50, 150)
racket_right = Player('racket.png', 520, 300, 4, 50, 150)

game = True
while game:
    racket_left.reset()
    racket_left.update()

    racket_right.reset()
    racket_right.update_2()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        pygame.display.update()
        clock.tick(60)
