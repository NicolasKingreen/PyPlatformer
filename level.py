import pygame

from window import Window
from tile import Tile
from player import Player
from camera import Camera

test_level_map = [
            '                        ',
            '                     X  ',
            '                        ',
            'X  XXXXXXXXXXXXXXX      ',
            'X         XXXXXXXX      ',
            'XXXX                    ',
            '     XXXXXX XXXXXXXX    ',
            'XXXXXX     P         X  ',
            '           XX   XXXXXXXX',
            '        XXXXXXX         ',
            'XXXXXXXXXXXXXXXXXXXXXXXX',
            'XXXXXXXXXXXXXXXXXXXXXXXX'
]


class Level:

    def __init__(self, level_map):
        self.map = test_level_map
        self.tiles = pygame.sprite.Group()
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                if cell == "X":
                    self.tiles.add(Tile((x, y)))
                elif cell == "P":
                    self.player = Player((x, y))

        self.width = len(self.map[0]) * Tile.WIDTH
        self.height = len(self.map) * Tile.HEIGHT

        self.camera = Camera(self.player)

    def x_shift(self, x_shift):
        for tile in self.tiles:
            tile.move(pygame.math.Vector2(x_shift, 0))

    def update(self, frame_time_s):
        # self.tiles.update(frame_time_s)
        if self.player.rect.centerx < 200 and self.player.move_direction.x < 0 and self.player.rect.centerx + self.camera.position.x > 500:
            self.player.x_speed = 0
            self.camera.x_speed = -128
        elif self.player.rect.centerx > Window.WIDTH - 200 and self.player.move_direction.x > 0 and self.player.rect.centerx + self.camera.position.x < self.width + 140:
            self.player.x_speed = 0
            self.camera.x_speed = 128
        else:
            self.player.x_speed = 128
            self.camera.x_speed = 0

        self.player.update(frame_time_s, self.tiles)
        self.camera.update(frame_time_s)
        for tile in self.tiles.sprites():
            tile.move(pygame.math.Vector2(-self.camera.x_speed * frame_time_s, 0))

    def draw(self, surface):
        self.tiles.draw(surface)
        self.player.draw(surface)

