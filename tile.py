import pygame

from settings import ZOOM_LEVEL


class Tile(pygame.sprite.Sprite):

    WIDTH, HEIGHT = SIZE = (32 * ZOOM_LEVEL, 32 * ZOOM_LEVEL)

    def __init__(self, position):
        super().__init__()
        position = (position[0] * Tile.WIDTH, position[1] * Tile.HEIGHT)
        self.image = pygame.Surface(Tile.SIZE)
        self.rect = self.image.get_rect(topleft=position)

    def move(self, vector):
        self.rect.center += vector

    def update(self, frame_time_s):
        pass
