import pygame
import settings
import sys
from .algorithms.breadth_first import BreadthFirst
from .algorithms.depth_first import DepthFirst


def drawGrid():
    for x in range(settings.cols):
        for y in range(settings.rows):
            rect = pygame.Rect(x*settings.blocksize, y*settings.blocksize, settings.blocksize, settings.blocksize)
            pygame.draw.rect(settings.SCREEN, settings.GREY, rect, 0)
     
    
def make_button(begin, end, col1, col2, mouse):
    if begin <= mouse[0] <= end and 0 <= mouse[1] <= settings.blocksize:
        pygame.draw.rect(settings.SCREEN, col2, [begin, 0, end - begin, settings.blocksize])
    else:
        pygame.draw.rect(settings.SCREEN, col1, [begin, 0, end-begin, settings.blocksize])
            

def handle_events():
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()    
                if settings.begin_go + 1 <= mouse[0] <= settings.end_go and 0 <= mouse[1] <= settings.blocksize and settings.GREEN_COOR and settings.RED_COOR:
                    r, c = settings.GREEN_COOR[0]
                    if settings.BFS_SELECTED:
                        dfs = DepthFirst(r, c)
                        dfs.run()
                        
                    else:
                        bfs = BreadthFirst(c, r)
                        bfs.run()
                    
                if  settings.begin_dfs+1 <= mouse[0] <= settings.end_dfs and 0 <= mouse[1] <= settings.blocksize:
                    settings.BFS_SELECTED = True
                        
                if settings.begin_bfs+1 <= mouse[0] <= settings.end_bfs and 0 <= mouse[1] <= settings.blocksize:
                    settings.BFS_SELECTED = False
                    
                if settings.begin_green+1 <= mouse[0] <= settings.end_green and 0 <= mouse[1] <= settings.blocksize and not settings.GREEN_COOR:
                    settings.COLOR = settings.GREEN
                    
                if settings.begin_wall+1 <= mouse[0] <= settings.end_wall and 0 <= mouse[1] <= settings.blocksize:
                    settings.COLOR = settings.BLUE
                    
                if settings.begin_red+1 <= mouse[0] <= settings.end_red and 0 <= mouse[1] <= settings.blocksize and not settings.RED_COOR:
                    settings.COLOR = settings.RED
                    
                if settings.begin_grey+1 <= mouse[0] <= settings.end_grey and 0 <= mouse[1] <= settings.blocksize:
                    settings.COLOR = settings.GREY
                    
                if settings.begin_removeAll+1 <= mouse[0] <= settings.end_removeAll and 0 <= mouse[1] <= settings.blocksize:
                    settings.COLOR = settings.BLUE
                    settings.RED_COOR = settings.GREEN_COOR = []
                    settings.positions = {}
                    for i in range(1, int(settings.height/settings.blocksize)):
                        for j in range(int(settings.width/settings.blocksize)):
                            settings.positions[(i, j)] = settings.GREY
                    while settings.HISTORY:
                        settings.HISTORY.pop()
                    drawGrid()
                    
                if settings.begin_back <= mouse[0] <= settings.end_back and 0 <= mouse[1] <= settings.blocksize:
                    if settings.HISTORY:
                        mpos_x, mpos_y, c = settings.HISTORY.pop()
                        coord = (mpos_x, mpos_y)
                        if [coord] == settings.GREEN_COOR:
                            settings.GREEN_COOR = []
                        if [coord] == settings.RED_COOR:
                            settings.RED_COOR = []
                        settings.COLOR = c
                        rect = pygame.Rect(coord[0]*settings.blocksize, coord[1]*settings.blocksize, settings.blocksize, settings.blocksize)
                        pygame.draw.rect(settings.SCREEN, settings.COLOR, rect)
                    else:
                        settings.COLOR = settings.BLUE
                        
                else:
                    if mouse[1]>settings.blocksize:
                        if settings.COLOR == settings.BLUE or settings.COLOR == settings.GREY:
                            mpos_x, mpos_y = pygame.mouse.get_pos()
                            coord = mpos_x // settings.blocksize, mpos_y // settings.blocksize
                            if settings.GREEN_COOR != [(coord[0], coord[1])] and settings.RED_COOR != [(coord[0], coord[1])]:
                                settings.HISTORY.append((mpos_x // settings.blocksize, mpos_y // settings.blocksize,
                                              settings.positions[(mpos_y // settings.blocksize, mpos_x // settings.blocksize)]))
                                settings.positions[(mpos_y // settings.blocksize, mpos_x // settings.blocksize)] = settings.COLOR

                                rect = pygame.Rect(coord[0] * settings.blocksize, coord[1] * settings.blocksize, settings.blocksize, settings.blocksize)
                                pygame.draw.rect(settings.SCREEN, settings.COLOR, rect)
                                
                        elif settings.COLOR == settings.GREEN and not settings.GREEN_COOR:
                            mpos_x, mpos_y = pygame.mouse.get_pos()
                            coord = mpos_x // settings.blocksize, mpos_y // settings.blocksize

                            settings.HISTORY.append((mpos_x // settings.blocksize, mpos_y // settings.blocksize,
                                          settings.positions[(mpos_y // settings.blocksize, mpos_x // settings.blocksize)]))
                            settings.positions[(mpos_y // settings.blocksize, mpos_x // settings.blocksize)] = settings.COLOR

                            rect = pygame.Rect(coord[0] * settings.blocksize, coord[1] * settings.blocksize, settings.blocksize, settings.blocksize)
                            pygame.draw.rect(settings.SCREEN, settings.COLOR, rect)
                            settings.GREEN_COOR = [(coord[0], coord[1])]

                        elif settings.COLOR == settings.RED and not settings.RED_COOR:
                            mpos_x, mpos_y = pygame.mouse.get_pos()
                            coord = mpos_x // settings.blocksize, mpos_y // settings.blocksize

                            settings.HISTORY.append((mpos_x // settings.blocksize, mpos_y // settings.blocksize,
                                          settings.positions[(mpos_y // settings.blocksize, mpos_x // settings.blocksize)]))
                            settings.positions[(mpos_y // settings.blocksize, mpos_x // settings.blocksize)] = settings.COLOR

                            rect = pygame.Rect(coord[0] * settings.blocksize, coord[1] * settings.blocksize, settings.blocksize, settings.blocksize)
                            pygame.draw.rect(settings.SCREEN, settings.COLOR, rect)
                            settings.RED_COOR = [(coord[0], coord[1])]

        mouse = pygame.mouse.get_pos()
        
        make_button(settings.begin_back, settings.end_back, settings.color_dark, settings.color_light,mouse)
        make_button(settings.begin_dfs, settings.end_dfs, settings.color_dark, settings.color_light,mouse)
        make_button(settings.begin_bfs, settings.end_bfs, settings.color_dark, settings.color_light,mouse)
        make_button(settings.begin_green, settings.end_green, settings.GREEN, settings.light_GREEN,mouse)
        make_button(settings.begin_wall, settings.end_wall, settings.BLUE, settings.light_BLUE,mouse)
        make_button(settings.begin_red, settings.end_red, settings.RED, settings.light_RED,mouse)
        make_button(settings.begin_grey, settings.end_grey, settings.GREY, settings.light_GREY,mouse)
        make_button(settings.begin_removeAll, settings.end_removeAll, settings.color_dark, settings.color_light,mouse)
        make_button(settings.begin_go, settings.end_go, settings.color_dark, settings.color_light,mouse)
        
        smallfont1 = pygame.font.SysFont('Corbel', settings.blocksize)
        smallfont2 = pygame.font.SysFont('Corbel', settings.blocksize//3)
        text = smallfont1.render('BACK' , True , settings.WHITE)
        text1 = smallfont1.render('REMOVE ALL' , True , settings.WHITE)
        text2a = smallfont1.render('DFS' , True , settings.GREEN)
        text2b = smallfont1.render('DFS' , True , settings.RED)
        text3a = smallfont1.render('BFS' , True , settings.GREEN)
        text3b = smallfont1.render('BFS' , True , settings.RED)
        text4 = smallfont1.render('FIND RED DOT' , True , settings.WHITE)

        settings.SCREEN.blit(text, (settings.begin_back + 10, 2))
        settings.SCREEN.blit(text1, (settings.begin_removeAll + 5, 2))
        settings.SCREEN.blit(text4, (settings.begin_go + 12, 2))
        if settings.BFS_SELECTED:
            settings.SCREEN.blit(text2a, (settings.begin_dfs + 5, 2))
            settings.SCREEN.blit(text3b, (settings.begin_bfs + 5, 2))

        else:
            settings.SCREEN.blit(text2b, (settings.begin_dfs + 5, 2 ))
            settings.SCREEN.blit(text3a, (settings.begin_bfs + 5, 2))
    
        pygame.draw.rect(settings.SCREEN, settings.WHITE, [settings.begin_bfs, 0, settings.end_bfs - settings.begin_bfs, settings.blocksize], 1)
        pygame.draw.rect(settings.SCREEN, settings.WHITE, [settings.begin_dfs, 0, settings.end_dfs - settings.begin_dfs, settings.blocksize], 1)
        pygame.draw.rect(settings.SCREEN, settings.WHITE, [settings.begin_back, 0, settings.end_back - settings.begin_back, settings.blocksize], 1)
        pygame.draw.rect(settings.SCREEN, settings.WHITE, [settings.begin_green, 0, settings.end_green - settings.begin_green, settings.blocksize], 1)
        pygame.draw.rect(settings.SCREEN, settings.WHITE, [settings.begin_wall, 0, settings.end_wall - settings.begin_wall, settings.blocksize], 1)
        pygame.draw.rect(settings.SCREEN, settings.WHITE, [settings.begin_red, 0, settings.end_red - settings.begin_red, settings.blocksize], 1)
        pygame.draw.rect(settings.SCREEN, settings.WHITE, [settings.begin_grey, 0, settings.end_grey - settings.begin_grey, settings.blocksize], 1)
        pygame.draw.rect(settings.SCREEN, settings.WHITE, [settings.begin_removeAll, 0, settings.end_removeAll - settings.begin_removeAll, settings.blocksize], 1)
        pygame.draw.rect(settings.SCREEN, settings.WHITE, [settings.begin_go, 0, settings.end_go - settings.begin_go, settings.blocksize], 1)
        pygame.display.update()