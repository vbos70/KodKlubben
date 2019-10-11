from random import choice, random, randrange
from game import *
import sys

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
        ((heading, dist),(target, fran)) = mv

        # check sailing distance
        if heading == 'N':
            if y + dist >= self.boardsize:
                result = False
        elif heading == 'E':
            if x + dist >= self.boardsize:
                result = False
        elif heading == 'S':
            if y - dist < 0:
                result = False
        elif heading == 'W':
            if x - dist < 0:
                result = False

        # cannot shoot backwards
        if target == 'N' and heading == 'S':
            return False
        if target == 'S' and heading == 'N':
            return False
        if target == 'E' and heading == 'W':
            return False
        if target == 'W' and heading == 'E':
            return False
       
        # check firing range
        if target == 'N':
            if y + fran >= self.boardsize:
                result = False
        elif target == 'E':
            if x + fran >= self.boardsize:
                result = False
        elif target == 'S':
            if y - fran < 0:
                result = False
        elif target == 'W':
            if x - fran < 0:
                result = False

        return result
    
    def possible_moves(self, bot):
        moves = []
        if self.hits[bot] < 3:

            directions = ['N', 'E', 'S', 'W']
            distances = [0, 1, 2]
            fire_ranges = [0, 1, 2]
            moves = [ ((heading, dist), (target, fran))
                      for heading in directions
                      for dist in distances
                      for target in directions
                      for fran in fire_ranges
                      if self.is_valid_move(((heading, dist),(target,fran)), bot) ]
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
        hit = False
        if move in self.possible_moves(bot):

            bot.move = move # so boatgame can use it to draw the boat
            
            ((heading, dist),(target, fran)) = move

            if fran > 0:
                tx, ty = self.position[bot]
                if target == 'N':
                    ty = ty + fran
                if target == 'E':
                    tx = tx + fran
                if target == 'S':
                    ty = ty - fran
                if target == 'W':
                    tx = tx - fran
                bot.tx_ty = (tx, ty) # so boatgame can use it to draw an explosion
                
                for b in self.bots:
                    if b != bot:
                        if self.is_boat_hit(b, (tx, ty), fran):
                            self.hits[b] = self.hits[b] + 1
                
            x, y = self.position[bot]
            if heading == 'N':
                y = y + dist
            elif heading == 'E':
                x = x + dist
            elif heading == 'S':
                y = y - dist
            elif heading == 'W':
                x = x - dist
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
        dx = p1[0]-p0[0]
        dy = p1[1]-p0[1]
        ds = []
        if dx < 0:
            ds.append('W')
        if dx > 0:
            ds.append('E')
        if dy < 0:
            ds.append('S')
        if dy > 0:
            ds.append('N')
        return ds

    def distance_to_enemy(self, bot):
        for b in self.bots:
            if b != bot:
                dx = abs(self.position[bot][0] - self.position[b][0])
                dy = abs(self.position[bot][1] - self.position[b][1])
                return dx + dy
            
    def where_is_enemy(self, bot):
        for b in self.bots:
            if b != bot:
                return self.directions(self.position[bot], self.position[b])
        return ["?"]

    def move_direction(self, move):
        ((heading,_),(_,_)) = move
        return heading

    def target_direction(self, move):
        ((_,_),(target,_)) = move
        return target

    def fires(self, move):
        ((_,_),(_,fran)) = move
        return fran > 0
        

