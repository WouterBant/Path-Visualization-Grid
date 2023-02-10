import time
import pygame
import settings
import heapq


class AStar:
    
    def __init__(self, row, col):
        self.visit = {(row, col)}
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.pq = [(float("inf"), 0, row, col)]
        heapq.heapify(self.pq)

    def run(self):
        while self.pq:
            cost, steps, row, col = heapq.heappop(self.pq)
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
                            return

                        rect = pygame.Rect(c * settings.blocksize, r * settings.blocksize, settings.blocksize, settings.blocksize)
                        pygame.draw.rect(settings.SCREEN, settings.light_GREEN, rect)
                        manhattan_distance = abs(settings.RED_COOR[0][1] - r) + abs(settings.RED_COOR[0][0] - c)
                        heapq.heappush(self.pq, (manhattan_distance+steps, steps+1, r, c))
                        self.visit.add((r, c))
