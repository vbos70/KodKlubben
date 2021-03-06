CSIZE = 80
BSIZE = 5
WIDTH = BSIZE * CSIZE
HEIGHT = BSIZE * CSIZE + CSIZE * 2
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

def color_dist(c1, c2):
   return sum([abs(s - t) ** 2 for (s,t) in zip(c1, c2)]) ** 0.5
   
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

def cells():
   for x in range(BSIZE):
      for y in range(BSIZE):
         yield (x, y)
                

board = init_board(BSIZE)
def draw():
   screen.fill(board_color)
   for (x, y) in cells():
      screen.draw.filled_rect(Rect((x*CSIZE, y*CSIZE), (CSIZE, CSIZE)),
                              board[y][x])
   for (x, y) in cells():
      screen.draw.rect(Rect((x*CSIZE, y*CSIZE), (CSIZE, CSIZE)),
                       (0,0,0))

   screen.draw.text("Score",
                    fontsize=CSIZE,
                    color=(0,0,0),
                    midtop=(BSIZE * CSIZE * 0.5, (BSIZE+0) * CSIZE))
   score = compute_score()
   screen.draw.text("{:d}".format(score[0]),
                    fontsize=CSIZE,
                    color=A_color,
                    midtop=(BSIZE * CSIZE * 0.3, (BSIZE+1) * CSIZE))
   screen.draw.text("{:d}".format(score[1]),
                    fontsize=CSIZE,
                    color=B_color,
                    midtop=(BSIZE * CSIZE * 0.7, (BSIZE+1) * CSIZE))

   
def compute_score():
   score = [0,0]
   for x, y in cells():
      clr = board[y][x]
      cdA = color_dist(clr, A_color)
      cdB = color_dist(clr, B_color)
      if cdA < cdB:
         score[0] += 1
      elif cdB < cdA:
         score[1] += 1
   return score

def show_end_score():
   for x, y in cells():
      clr = board[y][x]
      cdA = color_dist(clr, A_color)
      cdB = color_dist(clr, B_color)
      if cdA < cdB:
         board[y][x] = A_color
      elif cdB < cdA:
         board[y][x] = B_color
   draw()

def game_end():
   for x, y in cells():
      if board[y][x] == board_color:
         return False
   return True

player = [A_color, B_color]
turn = 0
def other(turn): return 1 - turn
def on_mouse_down(pos):
    global turn
    if game_end():
       show_end_score()
       return
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
