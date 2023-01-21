import pygame


def init():
    # Window
    global blocksize, width, height
    blocksize = 32
    width = 24 * blocksize
    height = 12 * blocksize

    # Colors
    global BLACK, GREY, RED, GREEN, BLUE, WHITE
    BLACK = (0, 0, 0)
    GREY = (200, 200, 200)
    RED = (200, 0, 0)
    GREEN = (0, 200, 0)
    BLUE = (0, 0, 200) 
    WHITE = (255,255,255)

    global light_GREY, light_RED, light_BLUE, light_GREEN
    light_GREY = (180, 180, 180)
    light_RED = (240,128,128)
    light_BLUE = (128, 128, 240) 
    light_GREEN = (128,240,128) 

    global color_light, color_dark
    color_light = (170,170,170)
    color_dark = (100,100,100)

    # Positions of the buttons (row 0)
    global begin_green, end_green, begin_wall, end_wall, begin_red, end_red, begin_grey, end_grey
    begin_green, end_green = 0, blocksize
    begin_wall, end_wall = blocksize, 2 * blocksize
    begin_red, end_red = 2 * blocksize, 3 * blocksize
    begin_grey, end_grey = 3 * blocksize, 4 * blocksize

    global begin_back, end_back, begin_removeAll, end_removeAll
    begin_back, end_back = 4 * blocksize, 7 * blocksize
    begin_removeAll, end_removeAll = 7 * blocksize, 13 * blocksize

    global begin_dfs, end_dfs, begin_bfs, end_bfs, begin_go, end_go
    begin_dfs, end_dfs = 13 * blocksize, 15 * blocksize
    begin_bfs, end_bfs = 15 * blocksize, 17 * blocksize
    begin_go, end_go = 17 * blocksize, 24 * blocksize

    # Make dictionary mapping grid coordinates to the color of the grid
    global positions
    positions = {}
    for i in range(1, int(height / blocksize)):
        for j in range(int(width / blocksize)):
            positions[(i, j)] = GREY

    # Rows and Columns
    global rows, cols
    rows = int(height / blocksize)
    cols = int(width / blocksize)

    # Back functionality
    global HISTORY
    HISTORY = []

    global COLOR, BFS_SELECTED, DFS_SELECTED
    COLOR = BLUE
    BFS_SELECTED = False
    DFS_SELECTED = False

    global RED_COOR, GREEN_COOR
    RED_COOR = []
    GREEN_COOR = []

    global SCREEN, CLOCK
    SCREEN = pygame.display.set_mode((width, height))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

