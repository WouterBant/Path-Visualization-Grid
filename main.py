import pygame
import codeVisualizer.events as ev
import settings

if __name__ == "__main__": 
    settings.init()
    pygame.init()
    ev.drawGrid()
    ev.handle_events()