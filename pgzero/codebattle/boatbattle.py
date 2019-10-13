from random import choice, random, randrange
from game import *
import sys

class Move:

    def __init__(self, heading, dist, target, fran):
        self.heading = heading
        self.dist = dist
        self.target = target
        self.fran = fran

    def __eq__(self, other):
        return ( self.heading == other.heading and
                 self.dist == other.dist and
                 self.target == other.target and
                 self.fran == other.fran )
    
class BoatBattle(Game):

    def __init__(self, boardsize, bots, max_turn = 0):
        super().__init__(bots)
        self.max_turn = max_turn
        self.max_hits = 3
        self.boardsize = boardsize
        self.position = { b : (randrange(boardsize),  randrange(self.boardsize)) for b in self.bots }
        self.hits = { b : 0 for b in self.bots }

    def is_valid_move(self, mv, bot):
        result = True
        x,y = self.position[bot]

        # check sailing distance
        if mv.heading == 'S':
            if y + mv.dist >= self.boardsize:
                result = False
        elif mv.heading == 'E':
            if x + mv.dist >= self.boardsize:
                result = False
        elif mv.heading == 'N':
            if y - mv.dist < 0:
                result = False
        elif mv.heading == 'W':
            if x - mv.dist < 0:
                result = False

        # cannot shoot backwards
        if mv.target == 'N' and mv.heading == 'S':
            result = False
        if mv.target == 'S' and mv.heading == 'N':
            result = False
        if mv.target == 'E' and mv.heading == 'W':
            result = False
        if mv.target == 'W' and mv.heading == 'E':
            result = False
       
        # check firing range
        if mv.target == 'S':
            if y + mv.fran >= self.boardsize:
                result = False
        elif mv.target == 'E':
            if x + mv.fran >= self.boardsize:
                result = False
        elif mv.target == 'N':
            if y - mv.fran < 0:
                result = False
        elif mv.target == 'W':
            if x - mv.fran < 0:
                result = False

        return result
    
    def possible_moves(self, bot):
        moves = []
        if self.hits[bot] < 3:

            directions = ['N', 'E', 'S', 'W']
            distances = [0, 1, 2]
            fire_ranges = [0, 1, 2]
            moves = [ Move(heading, dist, target, fran)
                      for heading in directions
                      for dist in distances
                      for target in directions
                      for fran in fire_ranges
                      if self.is_valid_move(Move(heading, dist, target,fran), bot) ]
        return moves

    def is_boat_hit(self, bot, target, fran):
        if self.old_position[bot] == target:
            # bot's position at the start of the turn is at target position
            d = { 1 : 0.9,    # close range fire has high probability of hit
                  2 : 0.65,   # medium range fire has lower probablity of hit
                  3: 0.25 }   # long range fire has low probability of hit
            return random() <= d[fran]
        # bot is not at target position
        return False
    
    def execute(self, bot, move):
        if move in self.possible_moves(bot):

            bot.move = move # so boatgame can use it to draw the boat
            
            if move.fran > 0:
                tx, ty = self.position[bot]
                if move.target == 'N':
                    ty = ty - move.fran
                if move.target == 'E':
                    tx = tx + move.fran
                if move.target == 'S':
                    ty = ty - move.fran
                if move.target == 'W':
                    tx = tx - move.fran
                bot.tx_ty = (tx, ty) # so boatgame can use it to draw an explosion
                for b in self.bots:
                    if b != bot:
                        if self.is_boat_hit(b, (tx, ty), move.fran):
                            self.hits[b] = self.hits[b] + 1
                
            x, y = self.position[bot]
            if move.heading == 'N':
                y = y - move.dist
            elif move.heading == 'E':
                x = x + move.dist
            elif move.heading == 'S':
                y = y + move.dist
            elif move.heading == 'W':
                x = x - move.dist
            self.position[bot] = (x,y)

            
    def play_turn(self):

        for b in self.bots:
            if self.hits[b] >= self.max_hits:
                self.stop_game = True
                return
            
        self.old_position = { b : self.position[b] for b in self.bots }
        for bot in self.bots:
            bot.step(self)
        self.turn = self.turn + 1

    def hit(self, bot):
        return self.hits[bot] 

    def directions(self, p0, p1):
        #  .(x0,y0)              E, S
        #          .(x1,y1)
        #
        x0, y0 = p0
        x1, y1 = p1
        ds = set()
        if x1 < x0:
            ds.add('W')
        elif x1 > x0:
            ds.add('E')
        if y1 < y0:
            ds.add('N')
        elif y1 > y0:
            ds.add('S')
        return ds

    def distance_to_enemy(self, bot):
        for b in self.bots:
            if b != bot:
                dx = abs(self.position[bot][0] - self.position[b][0])
                dy = abs(self.position[bot][1] - self.position[b][1])
                return dx + dy
            
    def where_is_enemy(self, bot):
        dirs = set()
        for b in self.bots:
            if b != bot:
                dirs.update(self.directions(self.position[bot], self.position[b]))
        return dirs
        

