import random

def generate_maze(sz):
   cells = [(x,y) for x in range(sz) for y in range(sz)]
   doors = {(c1, c2) : random.choice([True, False])
         for c1 in cells
         for c2 in cells
         if c1 < c2}
   return (sz, cells, doors)

def door_exists(c0, c1, mz):
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
         if r == 0 or not door_exists((r-1,c), (r,c), mz):
            l = l + ('+-')
         else:
            l = l + ('+ ')
      print(l + '+')
      l = ''
      for c in range(sz):
         if c == 0 or not door_exists((r,c-1), (r,c), mz):
            l = l + ('| ')
         else:
            l = l + ('  ')
      print(l + '|')
   print(('+-' * sz) + '+')         


def neighbours(c, mz):
   sz, cells, doors = mz
   x0, y0 = c
   nbrs = [(x1,y1) for (x1,y1) in [(x0-1,y0-1),
                                   (x0,y0-1),
                                   (x0+1,y0-1),
                                   (x0-1,y0),
                                   (x0+1,y0),
                                   (x0-1,y0+1),
                                   (x0,y0+1),
                                   (x0+1,y0+1)]
           if x1 >= 0 and x1 < sz  and y1 >= 0 and y1 < sz ]
   return nbrs
           
def find_path(mz, c0, c1):
   sz, cells, doors = mz

   # initialize distance to all cells to max value
   distance = { n : len(cells) for n in cells }

   # distance to start (c0) is 0
   distance[c0] = 0

   # find reachable neighbours
   nbrs = [c  for c in neighbours(c0, mz)
           if door_exists(c0, c, mz)]

   while len(nbrs)>0:
      n0 = nbrs[0]
      del nbrs[0]

      # find neighbours with door to/from n0      
      n1_nbrs = [ c for c in neighbours(n0, mz)
                  if door_exists(n0,c, mz)]
      # append each neighbour to the nbrs list
      for n1 in n1_nbrs:

         # and decrease the distance if possible
         if distance[n1] > distance[n0] + 1:
            distance[n1] = distance[n0] + 1
            nbrs.append(n1)
         
   return distance
   
if __name__ == '__main__':
   size_str = input('Size: ')
   maze_size = int(size_str)

   if maze_size > 0:
      mz = generate_maze(maze_size)
      print_maze(mz)

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
   else:
      print('Maze size should be greater than 0')
      

      
