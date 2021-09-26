import pygame

from settings import ZOOM_LEVEL


class Window:

    WIDTH, HEIGHT = DIMENSIONS = (640 * ZOOM_LEVEL, 360 * ZOOM_LEVEL)

    def __init__(self):
        self.surface = pygame.display.set_mode(Window.DIMENSIONS)
        pygame.display.set_caption("Platformer")

    # def update(self):
    #     self.surface.fill((255, 255, 255))
    #     pygame.display.update()
