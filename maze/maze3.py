import random
import sys
import turtle
import tkinter

def xcoord(c):
   return c[0]

def ycoord(c):
   return c[1]

def generate_maze(sz):
   cells = [(x,y) for x in range(sz) for y in range(sz)]
   doors = {(c1, c2) : random.choice([True, True, False])
            for c1 in cells
            if xcoord(c1) < sz - 1 and ycoord(c1) < sz - 1
            for c2 in [(xcoord(c1)+1, ycoord(c1)),
                       (xcoord(c1), ycoord(c1)+1)]}
   return (sz, cells, doors)

def door_exists(mz, c0, c1):
   sz, cells, doors = mz
   if (c0,c1) in doors:
      return doors[(c0,c1)]
   if (c1,c0) in doors:
      return doors[(c1,c0)]
   return False


def has_doors(mz, c):
   sz, cells, doors = mz
   for d in doors:
      if doors[d] and (c in d):
         return True
   return False
   
def cell_center(mz, cell):
   #sz, cells, doors = mz
   scale = image_scale()
   m = scale / 2
   return (xcoord(cell) * scale + m + draw_offset(mz),
           (ycoord(cell) * scale + m + draw_offset(mz)))

def image_scale():
   return 40

def draw_offset(mz):
   sz, cells, doors = mz
   return -1 * image_scale() * sz / 2

def ll_maze(mz):
   return (draw_offset(mz), draw_offset(mz))

def ur_maze(mz):
   return (-draw_offset(mz), -draw_offset(mz))
   

def draw_maze(mz):
   sz, cells, doors = mz
   scale = image_scale()

   for cx in range(sz):
      write_centered(mz, str(cx), (cx, -1))
      write_centered(mz, str(cx), (-1, cx))
      
   cv = turtle.getcanvas()

   for i in range(1, sz):
      cv.create_line(
         draw_offset(mz) + i * scale, draw_offset(mz),
         draw_offset(mz) + i * scale, -draw_offset(mz),         
         fill = 'DarkBlue',
         width = 5)
      cv.create_line(
         draw_offset(mz), draw_offset(mz) + i * scale,
         -draw_offset(mz), draw_offset(mz) + i * scale,         
         fill = 'DarkBlue',
         width = 5)

   for d in doors:
      if doors[d]:
         c0, c1 = d
         cc0 = cell_center(mz, c0)
         cc1 = cell_center(mz, c1)
         mx = (xcoord(cc0) + xcoord(cc1)) / 2
         my = (ycoord(cc0) + ycoord(cc1)) / 2

         cv.create_rectangle(mx-scale//6, my-scale//6,
                             mx+scale//6, my+scale//6,
                             fill='white', outline='white')

   for c in cells:
      if not has_doors(mz, c):
         cx, cy = cell_center(mz, c)
         cv.create_rectangle(cx-image_scale()/2, cy-image_scale()/2,
                             cx+image_scale()/2, cy+image_scale()/2,
                             fill='DarkBlue', outline='DarkBlue')
   ll = ll_maze(mz)
   ur = ur_maze(mz)
   cv.create_rectangle(xcoord(ll), ycoord(ll),
                       xcoord(ur), ycoord(ur),
                       outline = 'DarkBlue',
                       width = 5)

   
   
def write_centered(mz, s, c):
   sz, cells, doors = mz
   x, y = cell_center(mz, c)
   fontsz = image_scale()//3
   turtle.getcanvas().create_text(
      x, y,
      font=("Arial", fontsz, "normal"),
      text=s
      )

   
def draw_trail(mz, distance, c):
   sz, cells, doors = mz

   while distance[c] < sz*sz:
      print(c)
      
      # get center coordinates of cell c (the next line has to be fixed!)
      x, y = cell_center(mz, c)

      turtle.getcanvas().create_oval(x-image_scale()/4, y-image_scale()/4,
                                     x+image_scale()/4, y+image_scale()/4,
                                     fill='green', outline='red')
      
      # check if we have reached the start point
      if distance[c] == 0:
         break

      # find a neighbour at 1 step away
      for n in neighbours(mz,c):
         if door_exists(mz, c, n) and distance[n] + 1 == distance[c]:
            # note that the door_exists() check is redundant: if the
            # distance between c and n is 1, then there is a door
            # between c and n.
            c = n
            break
      # no check needed for case with no neighbours.

   
def draw_distance(mz, distance):
   sz, cells, doors = mz
   for r in range(sz):
      l = []
      for c in range(sz):
         if distance.get((c,r),sz*sz) < sz*sz:
            write_centered(mz, str(distance.get((c,r),'')), (c,r))

def neighbours(mz, c):
   sz, cells, doors = mz
   x0, y0 = c
   nbrs = [(x1,y1) for (x1,y1) in [(x0,   y0-1), # above
                                   (x0-1, y0),   # left
                                   (x0+1, y0),   # right
                                   (x0,   y0+1)  # below
   ]
           if x1 >= 0 and x1 < sz  and y1 >= 0 and y1 < sz ]
   return nbrs
           
def find_path(mz, c0, c1):
   sz, cells, doors = mz

   # initialize distance to all cells to max value
   distance = { n : sz * sz for n in cells }

   # distance to start (c0) is 0
   distance[c0] = 0

   # initialize queue
   queue = [c0]

   while len(queue)>0:
      c0 = queue[0]
      del queue[0]

      # find neighbours with door to/from n0
      for c1 in neighbours(mz, c0):
         if door_exists(mz, c0, c1):

            # check if path from c0 to c1 is shortest path to c1 sofar
            if distance[c1] > distance[c0] + 1:

               # if so, update distance to c1
               distance[c1] = distance[c0] + 1

               # and remember to compute paths from c1
               queue.append(c1)
               
   return distance


def int_input(msg, default=0):
   istr = input(msg).strip()
   if istr == '':
      print ('No integer given, taking %d' % default)
      return default
   for c in istr:
      if c not in ['0','1','2','3','4','5','6','7','8','9']:
         print('Illegal input character: ', c)
         return default
   return int(istr)

def coordinate_input(msg, default):
   c = int_input(msg, default)
   if not(c >= 0 and c < sz):
      print('Illegal coordinate: ', c, '(taking %d instead)' % default)
      return 0
   return c

if __name__ == '__main__':

   turtle.hideturtle()

   print (len(sys.argv))
   if len(sys.argv) == 3:
      num = int(sys.argv[1])
      sz = int(sys.argv[2])
      for round in range(1,num+1):
         random.seed(round)
      
         mz = generate_maze(sz)
         turtle.getcanvas().delete(tkinter.ALL)
         draw_maze(mz)

         ts = turtle.getscreen()
         fname = "mz%d_%d.eps" % (round, sz)
         ts.getcanvas().postscript(file=fname)
      sys.exit()
      
   elif len(sys.argv) != 1:
      print('Illegal usage')
      sys.exit()
      
   run = True
   maze_size = 4
   round = 0
   x0 = 0
   y0 = 0
   x1 = 0
   y1 = 0
   while run:
      maze_size = int_input('Size [%d]: ' % maze_size, maze_size)
      if maze_size < 1 or maze_size > 100:
         print('Maze size should be from 1 to 100.')
         maze_size = 4
         continue

      # check and set default (x1,y1) to valid point.
      if x1 <= 0 or x1 >= maze_size or y1 <= 0 or y1 >= maze_size:
         x1 = maze_size - 1
         y1 = maze_size - 1
      
      round = round + 1
      print ('Round ', round)
      random.seed(round)
      
      mz = generate_maze(maze_size)
      draw_maze(mz)

      sz, cells, doors = mz

      print()
      x0 = coordinate_input('x0 [%d]: ' % x0, x0)
      y0 = coordinate_input('y0 [%d]: ' % y0, y0)
      x1 = coordinate_input('x1 [%d]: ' % x1, x1)
      y1 = coordinate_input('y1 [%d]: ' % y1, y1)
      
      run = True
      d = find_path(mz, (x0, y0), (x1, y1))
      draw_distance(mz, d)
         
      if d[(x1,y1)] == sz * sz:
         print('There is no path between these cells.')
      else:
         print('Distance between (x0,y0) and (x1, y1) is: ', d[(x1,y1)])
         draw_trail(mz, d, (x1, y1))

      c = input('Again? ([Y]/N)').strip()
      if not(c == '' or c == 'y' or c == 'Y'):
         print('Bye!')
         break
      else:
         turtle.getcanvas().delete(tkinter.ALL)
