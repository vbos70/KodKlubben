import random
import sys
import turtle

def generate_maze(sz):
   cells = [(x,y) for x in range(sz) for y in range(sz)]
   doors = {(c1, c2) : random.choice([True, True, False])
         for c1 in cells
         for c2 in cells
         if c1 < c2}
   return (sz, cells, doors)

def door_exists(mz, c0, c1):
   sz, cells, doors = mz
   if (c0,c1) in doors:
      return doors[(c0,c1)]
   if (c1,c0) in doors:
      return doors[(c1,c0)]
   return False

def print_maze(mz):
   sz, cells, doors = mz
   for r in range(sz):
      l = ''
      for c in range(sz):
         if r == 0 or not door_exists(mz, (c, r-1), (c, r)):
            l = l + ('+-')
         else:
            l = l + ('+ ')
      print(l + '+')
      l = ''
      for c in range(sz):
         if c == 0 or not door_exists(mz, (c-1, r), (c,r)):
            l = l + ('| ')
         else:
            l = l + ('  ')
      print(l + '|')
   print(('+-' * sz) + '+')         

def cell_center(mz, cell):
   #sz, cells, doors = mz
   cx, cy = cell
   scale = draw_scale()
   m = scale / 2
   return (cx * scale + m - draw_offset(mz),
           -(cy * scale + m - draw_offset(mz)))


def draw_scale():
   return 40

def draw_offset(mz):
   sz, cells, doors = mz
   return draw_scale() * sz / 2

def draw_wall(scale):
   turtle.forward(scale)

def draw_door(scale):
   turtle.forward(scale / 4)
   turtle.penup()
   turtle.forward(scale / 2)
   turtle.pendown()
   turtle.forward(scale / 4)

def draw_footprint(scale):
   turtle.pendown()
   turtle.dot(scale / 2, 'green')

def draw_maze(mz):
   sz, cells, doors = mz
   scale = draw_scale()
   
   turtle.speed(speed = 0)
   turtle.showturtle()

   turtle.penup()
   turtle.setheading(0)
   turtle.backward(draw_offset(mz))
   turtle.setheading(270)
   turtle.backward(draw_offset(mz))
   
   
   for r in range(sz):
      for c in range(sz):
         turtle.setheading(270)
         turtle.pendown()
         if c == 0 or not door_exists(mz, (c-1, r), (c, r)):
            draw_wall(scale)
         else:
            draw_door(scale)


         turtle.penup()
         turtle.setheading(90)
         turtle.forward(scale)

         turtle.setheading(0)
         turtle.pendown()
         if r == 0 or not door_exists(mz, (c, r-1), (c,r)):
            draw_wall(scale)
         else:
            draw_door(scale)

      turtle.setheading(270)
      turtle.forward(scale)
      turtle.penup()
      turtle.setheading(180)
      turtle.forward(scale * sz)
   
   turtle.pendown()
   turtle.setheading(0)
   turtle.forward(scale * sz)

   for cx in range(sz):
      turtle.penup()
      x, y = cell_center(mz, (cx, -1))
      turtle.goto(x, y)
      turtle.write(str(cx), align='center', font=("Arial", 12, "normal"))

      turtle.penup()
      x, y = cell_center(mz, (-1, cx))
      fontsz = 12
      turtle.goto(x, y - fontsz/2)
      turtle.write(str(cx), align='center', font=("Arial", fontsz, "normal"))
   turtle.hideturtle()
   
def print_trail(mz, distance, c):
   sz, cells, doors = mz

   while distance[c] < sz*sz:
      print(c)

      # check if we have reached the start point
      if distance[c] == 0:
         break

      # find a neighbours at 1 step away
      for n in neighbours(mz,c):
         if door_exists(mz, c, n) and distance[n] + 1 == distance[c]:
            # note that the door_exists() check is redundant: if the
            # distance between c and n is 1, then there is a door
            # between c and n.
            c = n
            break
      # no check needed for case with no neighbours.

def draw_trail(mz, distance, c):
   sz, cells, doors = mz

   turtle.speed(speed = 6)

   while distance[c] < sz*sz:

      x, y = cell_center(mz, c)
      turtle.penup()
      turtle.goto(x, y)
      draw_footprint(draw_scale())

      # check if we have reached the start point
      if distance[c] == 0:
         break

      # find a neighbours at 1 step away
      for n in neighbours(mz,c):
         if door_exists(mz, c, n) and distance[n] + 1 == distance[c]:
            # note that the door_exists() check is redundant: if the
            # distance between c and n is 1, then there is a door
            # between c and n.
            c = n
            break
      # no check needed for case with no neighbours.

   
def print_distance(mz, distance):
   sz, cells, doors = mz
   for r in range(sz):
      l = []
      for c in range(sz):
         l.append(str(distance[(r,c)]))
      print(', '.join(l))

def draw_distance(mz, distance):
   # use turtle.write() to print the cell distances 
   pass

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
   
if __name__ == '__main__':

   print (len(sys.argv))
   if len(sys.argv) == 3:
      num = int(sys.argv[1])
      sz = int(sys.argv[2])
      for round in range(1,num+1):
         random.seed(round)
      
         mz = generate_maze(sz)
         turtle.reset()
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
   while run:
      size_str = input('Size [%d]: ' % maze_size).strip()
      if size_str != '':
         maze_size = int(size_str)
         
      if maze_size < 1 or maze_size > 100:
         print('Maze size should be from 1 to 100.')
         maze_size = 4
         continue
      
      round = round + 1
      print ('Round ', round)
      random.seed(round)
      
      mz = generate_maze(maze_size)
      print_maze(mz)
      turtle.reset()
      draw_maze(mz)

      ts = turtle.getscreen()

      ts.getcanvas().postscript(file="round_%d_%d.eps" % (round, maze_size))
      
      sz, cells, doors = mz
   
      print()
      x0_str = input('x0: ')
      y0_str = input('y0: ')
      x0, y0 = int(x0_str), int(y0_str)

      x1_str = input('x1: ')
      y1_str = input('y1: ')
      x1, y1 = int(x1_str), int(y1_str)

      run = False
      if not(x0 >= 0 and x0 < sz):
         print('Illegal x0 coordinate: ' + x0)
      elif not(y0 >= 0 and y0 < sz):
         print('Illegal y0 coordinate: ' + y0)
      elif not(x1 >= 0 and x1 < sz):
         print('Illegal x1 coordinate: ' + x1)
      elif not(y1 >= 0 and y1 < sz):
         print('Illegal y1 coordinate: ' + y1)
      else:
         run = True
         d = find_path(mz, (x0, y0), (x1, y1))
         print_distance(mz, d)
         
         if d[(x1,y1)] == sz * sz:
            print('There is no path between these cells.')
         else:
            print('Distance between (x0,y0) and (x1, y1) is: ', d[(x1,y1)])
            print('Trail:')
            print_trail(mz, d, (x1, y1))
            draw_trail(mz, d, (x1, y1))

      c = input('Again? ([Y]/N)').strip()
      if not(c == '' or c == 'y' or c == 'Y'):
         print('Bye!')
         break
