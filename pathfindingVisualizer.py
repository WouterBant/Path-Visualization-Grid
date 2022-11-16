import pygame
import sys # for exiting pygame window --- sys.exit()
import time # showing path finding procedure on a speed eyes can keep up with --- time.sleep(0.1)
import collections # queue for BFS --- collections.deque()

# Window
blocksize = 32
width = 24 * blocksize
height = 12 * blocksize

# Colors
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
light_GREY = (180, 180, 180)
RED = (200, 0, 0)
light_RED = (240,128,128)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200) 
light_BLUE = (128, 128, 240) 
WHITE = (255,255,255)
light_GREEN = (128,240,128) 
color_light = (170,170,170)
color_dark = (100,100,100)

# Positions of the buttons (row 0)
begin_green, end_green = 0, blocksize
begin_wall, end_wall = blocksize, 2 * blocksize
begin_red, end_red = 2 * blocksize, 3 * blocksize
begin_grey, end_grey = 3 * blocksize, 4 * blocksize
begin_back, end_back = 4 * blocksize, 7 * blocksize
begin_removeAll, end_removeAll = 7 * blocksize, 13 * blocksize
begin_dfs, end_dfs = 13 * blocksize, 15 * blocksize
begin_bfs, end_bfs = 15 * blocksize, 17 * blocksize
begin_go, end_go = 17 * blocksize, 24 * blocksize

# Make dictionary mapping grid coordinates to the color of the grid
dic = {}
for i in range(1, int(height / blocksize)):
    for j in range(int(width / blocksize)):
        dic[(i, j)] = GREY
        
# Make stack to keep track of last added positions and colors for back button
stack = []

BFS_SELECTED = [True]
REDFOUND = [False]

# Traversal directions (only horizontal and vertical)
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs(r, c):
    visit_bfs = set()
    visit_bfs.add((r, c))
    q = collections.deque()
    q.append((r, c))
    
    while q and not REDFOUND[0]:
        row, col = q.popleft()
        time.sleep(0.1)
        pygame.display.update()
        for dr, dc in directions:
            r, c = row + dr, col + dc
                    
            if (r in range(1, int(height / blocksize)) and c in range(int(width / blocksize))
                and (r,c) not in visit_bfs and dic[(r, c)] != BLUE):
                    if dic[(r, c)] == RED:
                        REDFOUND[0] = True
                        rect = pygame.Rect(c * blocksize, r * blocksize, blocksize, blocksize)
                        pygame.draw.rect(SCREEN, light_RED, rect)
                        pygame.display.update()
                        break

                    rect = pygame.Rect(c * blocksize, r * blocksize, blocksize, blocksize)
                    pygame.draw.rect(SCREEN, light_GREEN, rect)

                    q.append((r, c))
                    visit_bfs.add((r, c))

visit_dfs = set()
def dfs(r, c):
    if (r not in range(1, int(height / blocksize))
        or c not in range(int(width / blocksize))
        or dic[(r, c)] == BLUE or (r, c) in visit_dfs
        or REDFOUND[0]):
        return
    
    if dic[(r, c)] == RED:
        rect = pygame.Rect(c * blocksize, r * blocksize, blocksize, blocksize)
        pygame.draw.rect(SCREEN, light_RED, rect)
        pygame.display.update()
        REDFOUND[0] = True
        
    visit_dfs.add((r, c))
    rect = pygame.Rect(c * blocksize, r * blocksize, blocksize, blocksize)

    if not REDFOUND[0]:
        if dic[(r, c)] != GREEN:
            pygame.draw.rect(SCREEN, light_GREEN, rect)
            time.sleep(0.1)
            pygame.display.update()
            
        for dr, dc in directions:
            dfs(r + dr, c + dc)

def drawGrid(h, w, blocksize):
    for x in range(w):
        for y in range(h):
            rect = pygame.Rect(x*blocksize, y*blocksize, blocksize, blocksize)
            pygame.draw.rect(SCREEN, GREY, rect, 0)
     
    
def make_button(begin, end, col1, col2, mouse):
    if begin <= mouse[0] <= end and 0 <= mouse[1] <= blocksize:
        pygame.draw.rect(SCREEN, col2, [begin, 0, end - begin, blocksize])

    else:
        pygame.draw.rect(SCREEN, col1, [begin, 0, end-begin, blocksize])
            

def handle_events(blocksize):
    col = [BLUE]
    # Keep track where the green grid is (starting position)
    green_coor = []

    # Keep track where the red grid is (final position)
    red_coor = []
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()    
                if begin_go + 1 <= mouse[0] <= end_go and 0 <= mouse[1] <= blocksize and green_coor and red_coor:
                    r, c = green_coor[0]
                    if BFS_SELECTED[0]:
                        dfs(c, r)
                        
                    else:
                        bfs(c, r)
                    
                if  begin_dfs+1 <= mouse[0] <= end_dfs and 0 <= mouse[1] <= blocksize:
                    BFS_SELECTED[0] = True
                        
                if begin_bfs+1 <= mouse[0] <= end_bfs and 0 <= mouse[1] <= blocksize:
                    BFS_SELECTED[0] = False
                    
                if begin_green+1 <= mouse[0] <= end_green and 0 <= mouse[1] <= blocksize and not green_coor:
                    col = [GREEN]
                    
                if begin_wall+1 <= mouse[0] <= end_wall and 0 <= mouse[1] <= blocksize:
                    col = [BLUE]
                    
                if begin_red+1 <= mouse[0] <= end_red and 0 <= mouse[1] <= blocksize and not red_coor:
                    col = [RED]
                    
                if begin_grey+1 <= mouse[0] <= end_grey and 0 <= mouse[1] <= blocksize:
                    col = [GREY]
                    
                if begin_removeAll+1 <= mouse[0] <= end_removeAll and 0 <= mouse[1] <= blocksize:
                    col = [BLUE]
                    red_coor = green_coor = []
                    global visit_dfs
                    visit_dfs = set()
                    global visit_bfs
                    visit_bfs = set()
                    global dic 
                    dic = {}
                    for i in range(1, int(height/blocksize)):
                        for j in range(int(width/blocksize)):
                            dic[(i, j)] = GREY
                    while stack:
                        stack.pop()
                    drawGrid(height, width, blocksize)
                    REDFOUND[0] = False
                    
                if begin_back <= mouse[0] <= end_back and 0 <= mouse[1] <= blocksize:
                    if stack:
                        mpos_x, mpos_y, c = stack.pop()
                        coord = (mpos_x, mpos_y)
                        if [coord] == green_coor:
                            green_coor = []
                        if [coord] == red_coor:
                            red_coor = []
                        col = [c]
                        rect = pygame.Rect(coord[0]*blocksize, coord[1]*blocksize, blocksize, blocksize)
                        pygame.draw.rect(SCREEN, col[0], rect)
                    else:
                        col = [BLUE]
                        
                else:
                    if mouse[1]>blocksize:
                        if col[0] == BLUE or col[0] == GREY:
                            mpos_x, mpos_y = pygame.mouse.get_pos()
                            coord = mpos_x // blocksize, mpos_y // blocksize
                            if green_coor != [(coord[0], coord[1])] and red_coor != [(coord[0], coord[1])]:
                                stack.append((mpos_x // blocksize, mpos_y // blocksize,
                                              dic[(mpos_y // blocksize, mpos_x // blocksize)]))
                                dic[(mpos_y // blocksize, mpos_x // blocksize)] = col[0]

                                rect = pygame.Rect(coord[0] * blocksize, coord[1] * blocksize, blocksize, blocksize)
                                pygame.draw.rect(SCREEN, col[0], rect)
                                
                        elif col[0] == GREEN and not green_coor:
                            mpos_x, mpos_y = pygame.mouse.get_pos()
                            coord = mpos_x // blocksize, mpos_y // blocksize

                            stack.append((mpos_x // blocksize, mpos_y // blocksize,
                                          dic[(mpos_y // blocksize, mpos_x // blocksize)]))
                            dic[(mpos_y // blocksize, mpos_x // blocksize)] = col[0]

                            rect = pygame.Rect(coord[0] * blocksize, coord[1] * blocksize, blocksize, blocksize)
                            pygame.draw.rect(SCREEN, col[0], rect)
                            green_coor = [(coord[0], coord[1])]

                        elif col[0] == RED and not red_coor:
                            mpos_x, mpos_y = pygame.mouse.get_pos()
                            coord = mpos_x // blocksize, mpos_y // blocksize

                            stack.append((mpos_x // blocksize, mpos_y // blocksize,
                                          dic[(mpos_y // blocksize, mpos_x // blocksize)]))
                            dic[(mpos_y // blocksize, mpos_x // blocksize)] = col[0]

                            rect = pygame.Rect(coord[0] * blocksize, coord[1] * blocksize, blocksize, blocksize)
                            pygame.draw.rect(SCREEN, col[0], rect)
                            red_coor = [(coord[0], coord[1])]

        mouse = pygame.mouse.get_pos()
        
        make_button(begin_back, end_back, color_dark, color_light,mouse)
        make_button(begin_dfs, end_dfs, color_dark, color_light,mouse)
        make_button(begin_bfs, end_bfs, color_dark, color_light,mouse)
        make_button(begin_green, end_green, GREEN, light_GREEN,mouse)
        make_button(begin_wall, end_wall, BLUE, light_BLUE,mouse)
        make_button(begin_red, end_red, RED, light_RED,mouse)
        make_button(begin_grey, end_grey, GREY, light_GREY,mouse)
        make_button(begin_removeAll, end_removeAll, color_dark, color_light,mouse)
        make_button(begin_go, end_go, color_dark, color_light,mouse)
        
        smallfont1 = pygame.font.SysFont('Corbel', blocksize)
        smallfont2 = pygame.font.SysFont('Corbel', blocksize//3)
        text = smallfont1.render('BACK' , True , WHITE)
        text1 = smallfont1.render('REMOVE ALL' , True , WHITE)
        text2a = smallfont1.render('DFS' , True , GREEN)
        text2b = smallfont1.render('DFS' , True , RED)
        text3a = smallfont1.render('BFS' , True , GREEN)
        text3b = smallfont1.render('BFS' , True , RED)
        text4 = smallfont1.render('FIND RED DOT' , True , WHITE)

        SCREEN.blit(text, (begin_back + 10, 2))
        SCREEN.blit(text1, (begin_removeAll + 5, 2))
        SCREEN.blit(text4, (begin_go + 12, 2))
        if BFS_SELECTED[0]:
            SCREEN.blit(text2a, (begin_dfs + 5, 2))
            SCREEN.blit(text3b, (begin_bfs + 5, 2))

        else:
            SCREEN.blit(text2b, (begin_dfs + 5, 2 ))
            SCREEN.blit(text3a, (begin_bfs + 5, 2))
    
        pygame.draw.rect(SCREEN, WHITE, [begin_bfs, 0, end_bfs - begin_bfs, blocksize], 1)
        pygame.draw.rect(SCREEN, WHITE, [begin_dfs, 0, end_dfs - begin_dfs, blocksize], 1)
        pygame.draw.rect(SCREEN, WHITE, [begin_back, 0, end_back - begin_back, blocksize], 1)
        pygame.draw.rect(SCREEN, WHITE, [begin_green, 0, end_green - begin_green, blocksize], 1)
        pygame.draw.rect(SCREEN, WHITE, [begin_wall, 0, end_wall - begin_wall, blocksize], 1)
        pygame.draw.rect(SCREEN, WHITE, [begin_red, 0, end_red - begin_red, blocksize], 1)
        pygame.draw.rect(SCREEN, WHITE, [begin_grey, 0, end_grey - begin_grey, blocksize], 1)
        pygame.draw.rect(SCREEN, WHITE, [begin_removeAll, 0, end_removeAll - begin_removeAll, blocksize], 1)
        pygame.draw.rect(SCREEN, WHITE, [begin_go, 0, end_go - begin_go, blocksize], 1)
        pygame.display.update()
        

def main():
    global SCREEN, CLOCK, blocksize
    
    pygame.init()
    SCREEN = pygame.display.set_mode((width, height))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    drawGrid(height,width,blocksize)
    handle_events(blocksize)

if __name__ == "__main__": 
    main()