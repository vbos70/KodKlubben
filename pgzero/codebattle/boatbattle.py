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
            fire_ranges = [0, 1, 2, 3]
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
                  3: 0.25 }   # long range  fire has low probability of hit
            return random() <= d[fran]
        # bot is not at target position
        return False
    
    def execute(self, bot, move):
        hit = False
        if move in self.possible_moves(bot):

            msg = "Bot {bot} ".format(bot = bot.image)

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

                msg = msg + "fires at {target} and ".format(target = (tx,ty))

                for b in self.bots:
                    if b != bot:
                        if self.is_boat_hit(b, (tx, ty), fran):
                            self.hits[b] = self.hits[b] + 1
                            msg = msg + "bot {bot0} is hit! Bot {bot1} ".format(bot0 = b.image, bot1 = bot.image)
                            #hit = True
                        else:
                            msg = msg + "misses. Bot {bot} ".format(bot = bot.image)
                
            x, y = self.position[bot]
            if heading == 'N':
                y = y + dist
            elif heading == 'E':
                x = x + dist
            elif heading == 'S':
                y = y - dist
            elif heading == 'W':
                x = x - dist

            if dist > 0:
                msg = msg + "moves from {pos0} to {pos1}.".format( pos0 = self.position[bot], pos1 = (x,y))
            else:
                msg = msg + "stays at {pos}.".format( pos = (x,y))


            self.position[bot] = (x,y)
            if hit:    
                s = input(msg)
            else:
                print(msg)

            
    def play_turn(self):

        for b in self.bots:
            if self.hits[b] >= self.max_hits:
                self.stop_game = True
                return
            
        self.old_position = { b : self.position[b] for b in self.bots }
        for bot in self.bots:
            bot.step(self)
        self.turn = self.turn + 1
            

    def show_game(self):
        print("-"*40)
        if self.max_turn > 0:
            print("TURN", self.turn, "OF", self.max_turn)
        else:
            print("TURN:", self.turn)
        for b in self.bots:
            print( "Bot {img} {nm} [hits: {hits}]".format(img = b.image, nm = b.name, hits = self.hits[b]))
            
if __name__ == '__main__':

    b1 = Bot()
    b1.image = '*'
    b1.name = "B1"
    
    b2 = Bot()
    b2.image = '.'
    b2.name = "B2"

    interactive = False
    if len(sys.argv)>1:
        for a in sys.argv[1:]:
            if a == "-i":
                interactive = True
    game = BoatBattle(19,  [b1, b2], max_turn = 1000)
    game.run(interactive = interactive)

