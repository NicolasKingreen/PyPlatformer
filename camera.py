import pygame


class Camera:

    def __init__(self, player):
        self.position = pygame.math.Vector2((player.rect.centerx, player.rect.centery))
        self.x_speed = 0

    def update(self, frame_time_s):
        self.position.x += self.x_speed * frame_time_s
