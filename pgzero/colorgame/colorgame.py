CSIZE = 20
BSIZE = 10
WIDTH = BSIZE * CSIZE
HEIGHT = BSIZE * CSIZE

board_color = (250, 240, 240)
A_color = (255, 0, 0)
B_color = (0, 0, 255)

def init_board(size):
    return [[board_color for x in range(BSIZE)]
            for y in range(BSIZE)]

board = init_board(BSIZE)
def draw():
    for x in range(BSIZE):
        for y in range(BSIZE):
            screen.draw.filled_rect(Rect((x*CSIZE, y*CSIZE), (CSIZE, CSIZE)),
                                    board[y][x])

players = [A_color, B_color]
turn = 0
def on_mouse_down(pos):
    global turn
    x = pos[0] // CSIZE
    y = pos[1] // CSIZE
    if board[y][x] == board_color:
        board[y][x] = players[turn]

    turn = 1 - turn
    
    
