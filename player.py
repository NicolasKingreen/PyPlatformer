import pygame

from settings import ZOOM_LEVEL
from tile import Tile


class Player(pygame.sprite.Sprite):

    WIDTH, HEIGHT = SIZE = (16 * ZOOM_LEVEL, 32 * ZOOM_LEVEL)

    def __init__(self, position):
        super().__init__()
        position = position[0] * Tile.WIDTH + (Tile.WIDTH - Player.WIDTH) // 2, position[1] * Tile.HEIGHT
        self.image = pygame.Surface(Player.SIZE)
        self.image.fill((127, 127, 127))
        self.rect = self.image.get_rect(topleft=position)

        # movement
        self.x_speed = 128
        self.y_speed = 0
        self.jump_speed = 256
        self.gravity_acceleration = 512
        self.move_direction = pygame.math.Vector2()

    def process_keydown(self, key):
        if key == pygame.K_d:
            self.move_direction.x += 1
        elif key == pygame.K_a:
            self.move_direction.x -= 1
        elif key == pygame.K_w:
            self.jump()

    def process_keyup(self, key):
        if key == pygame.K_d:
            self.move_direction.x -= 1
        elif key == pygame.K_a:
            self.move_direction.x += 1

    def check_collision(self, tiles):
        pass

    def jump(self):
        self.y_speed = -self.jump_speed

    def update(self, frame_time_s, tiles):

        # x movement
        self.rect.x += self.move_direction.x * self.x_speed * frame_time_s
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.move_direction.x < 0:
                    self.rect.left = tile.rect.right
                elif self.move_direction.x > 0:
                    self.rect.right = tile.rect.left

        # y movement
        self.rect.y += self.y_speed * frame_time_s
        self.y_speed += self.gravity_acceleration * frame_time_s
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.y_speed > 0:
                    self.rect.bottom = tile.rect.top
                    self.y_speed = 0
                elif self.y_speed < 0:
                    self.y_speed = 0
                    self.rect.top = tile.rect.bottom

    def draw(self, surface):
        surface.blit(self.image, self.rect)
