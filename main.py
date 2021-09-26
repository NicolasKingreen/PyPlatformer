import pygame

from window import Window
from level import Level


class Platformer:

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.window = Window()
        self.level = Level(None)

        self.is_running = False

    def run(self):
        self.is_running = True
        while self.is_running:

            frame_time_ms = self.clock.tick(30)
            frame_time_s = frame_time_ms / 1000.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.stop()

                    self.level.player.process_keydown(event.key)

                    if event.key == pygame.K_RIGHT:
                        self.level.shift(32)
                    elif event.key == pygame.K_LEFT:
                        self.level.shift(-32)

                elif event.type == pygame.KEYUP:
                    self.level.player.process_keyup(event.key)

            self.level.update(frame_time_s)

            self.window.surface.fill((255, 255, 255))
            self.level.draw(self.window.surface)
            pygame.display.update()

    def stop(self):
        self.is_running = False
        pygame.quit()
        exit()


if __name__ == "__main__":
    Platformer().run()
