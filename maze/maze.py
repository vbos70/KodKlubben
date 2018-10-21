import random
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
         if r == 0 or not door_exists(mz, (r-1,c), (r,c)):
            l = l + ('+-')
         else:
            l = l + ('+ ')
      print(l + '+')
      l = ''
      for c in range(sz):
         if c == 0 or not door_exists(mz, (r,c-1), (r,c)):
            l = l + ('| ')
         else:
            l = l + ('  ')
      print(l + '|')
   print(('+-' * sz) + '+')         


   
def draw_wall(scale):
   turtle.forward(scale)

def draw_door(scale):
   turtle.forward(scale / 4)
   turtle.penup()
   turtle.forward(scale / 2)
   turtle.pendown()
   turtle.forward(scale / 4)
   
def draw_maze(mz):
   sz, cells, doors = mz

   turtle.speed(speed = 0)
   scale = 40

   turtle.penup()
   turtle.setheading(0)
   turtle.backward(scale * sz / 2)
   turtle.setheading(270)
   turtle.backward(scale * sz / 2)
   
   
   for r in range(sz):
      for c in range(sz):
         turtle.setheading(270)
         turtle.pendown()
         if c == 0 or not door_exists(mz, (r, c-1), (r, c)):
            draw_wall(scale)
         else:
            draw_door(scale)
         turtle.penup()
         turtle.setheading(90)
         turtle.forward(scale)

         turtle.setheading(0)
         turtle.pendown()
         if r == 0 or not door_exists(mz, (r-1,c), (r,c)):
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
   nbrs = [(x1,y1) for (x1,y1) in [#(x0-1, y0-1),
                                   (x0,   y0-1),
                                   #(x0+1, y0-1),
                                   (x0-1, y0),
                                   (x0+1, y0),
                                   #(x0-1, y0+1),
                                   (x0,   y0+1),
                                   #(x0+1, y0+1)
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
   size_str = input('Size: ')
   maze_size = int(size_str)

   if maze_size > 0:
      mz = generate_maze(maze_size)
      print_maze(mz)
      draw_maze(mz)
      
      sz, cells, doors = mz
      
      print()

      run = True
      while run:
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
            if d == sz * sz:
               print('There is no path between these cells.')
            else:
               print('Distance between (x0,y0) and (x1, y1) is: ', d[(x1,y1)])
            print_distance(mz, d)
   else:
      print('Maze size should be greater than 0')
      

      
