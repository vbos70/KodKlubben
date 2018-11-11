import random
import time

# comment out the following line if no reproducability is needed.
random.seed()

def rnd_size():
   return random.randint(6,30)

def rnd_coord(mz):
   sz, cells, doors = mz
   return random.randint(0, sz - 1)

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

