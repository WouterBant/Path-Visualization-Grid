import time
import pygame
import settings


class DepthFirst:

    def __init__(self, row, col):
        self.visit = {(row, col)}
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def run(self, row, col):
        time.sleep(0.1)
        pygame.display.update()
        for dr, dc in self.directions:
            r, c = row + dr, col + dc
                    
            if (r in range(1, settings.rows) and c in range(settings.cols)
                and (r, c) not in self.visit and settings.positions[(r, c)] != settings.BLUE):
                    if settings.positions[(r, c)] == settings.RED:
                        rect = pygame.Rect(c * settings.blocksize, r * settings.blocksize, settings.blocksize, settings.blocksize)
                        pygame.draw.rect(settings.SCREEN, settings.light_RED, rect)
                        pygame.display.update()
                        return True

                    rect = pygame.Rect(c * settings.blocksize, r * settings.blocksize, settings.blocksize, settings.blocksize)
                    pygame.draw.rect(settings.SCREEN, settings.light_GREEN, rect)

                    
                    self.visit.add((r, c))
                    solution = self.run(r, c)
                    if solution:
                        return True
    