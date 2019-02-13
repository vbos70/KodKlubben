CSIZE = 20
BSIZE = 10
WIDTH = BSIZE * CSIZE
HEIGHT = BSIZE * CSIZE
COLOR_F = 2
board_color = (255, 255, 255)
A_color = (255, 0, 0)
B_color = (0, 0, 255)


def color_range(start, end, num):
   if num < 2:
      return [start, end]
   r0, g0, b0 = start
   r1, g1, b1 = end
   dr = (r1 - r0) / (num-1)
   dg = (g1 - g0) / (num-1)
   db = (b1 - b0) / (num-1)
   return [ (round(r0 + i * dr),
             round(g0 + i * dg),
             round(b0 + i * db)) for i in range(num)]

def add_colors(c1, c2):
    r = (c1[0] + c2[0]) // 2
    g = (c1[1] + c2[1]) // 2
    b = (c1[2] + c2[2]) // 2
    return (r, g, b)

def dim_color(c, f):
    return tuple(c[i] // f for i in range(3))

def init_board(size):
    return [[board_color for x in range(BSIZE)]
            for y in range(BSIZE)]

def is_empty(cell):
   return cell == board_color

def neighbours(bsize, x, y):
    return [ (nx, ny) for (nx, ny) in
             [(x-1, y-1),
              (x-1, y),
              (x-1, y+1),
              (x, y-1),
              (x, y+1),
              (x+1, y-1),
              (x+1, y),
              (x+1, y+1)] if nx > -1 and nx < bsize and ny > -1 and ny < bsize ]


board = init_board(BSIZE)
def draw():
    for x in range(BSIZE):
        for y in range(BSIZE):
            screen.draw.filled_rect(Rect((x*CSIZE, y*CSIZE), (CSIZE, CSIZE)),
                                    board[y][x])

player = [A_color, B_color]
turn = 0
def other(turn): return 1 - turn
def on_mouse_down(pos):
    global turn
    x = pos[0] // CSIZE
    y = pos[1] // CSIZE
    if board[y][x] != player[other(turn)]:
        board[y][x] = player[turn]
        for nx, ny in neighbours(BSIZE, x, y):
            board[ny][nx] = add_colors(board[ny][nx],
                                       dim_color(player[turn], COLOR_F))
        turn = other(turn)
    
    
if __name__ == '__main__':
    print(add_colors(board_color, dim_color(player[turn], 4)))
    print(add_colors(player[other(turn)], dim_color(player[turn], 4)))
