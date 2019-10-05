from random import choice, randrange
from game import *
import sys

class BoatBattle(Game):

    def __init__(self, boardsize, bots, max_turn = 0):
        super().__init__(bots)
        self.max_turn = max_turn
        self.boardsize = boardsize
        self.position = { b : (randrange(boardsize),  randrange(self.boardsize)) for b in self.bots }
        self.hits = { b : 0 for b in self.bots }


    def possible_moves(self, bot):
        moves = []
        if self.hits[bot] < 3:
            x,y = self.position[bot]
            xs = [ x-d for d in [2,1] if x-d > 0 ] + [ x+d for d in [1,2] if x+d < self.boardsize ]
            ys = [ y-d for d in [2,1] if y-d > 0 ] + [ y+d for d in [1,2] if y+d < self.boardsize ]
            moves = [(i,y) for i in xs] + [(x,y)] + [(x,j) for j in ys]
        return moves

    def execute(self, bot, move):
        if move in self.possible_moves(bot):
            x, y = move
            if move != self.position[bot]:
                print("{bot}: Hits {hits}, Moves from {pos0} to {pos1}.".format(
                    bot = bot.image,
                    hits = self.hits[bot],
                    pos0 = self.position[bot],
                    pos1 = move))
            else:
                print("{bot}: Hits {hits}, Stays at {pos0}.".format(
                    bot = bot.image,
                    hits = self.hits[bot],
                    pos0 = self.position[bot]))
            self.position[bot] = (x, y)

    def show_game(self):
        print("-"*40)
        if self.max_turn > 0:
            print("TURN", self.turn, "OF", self.max_turn)
        else:
            print("TURN:", self.turn)
        for b in self.bots:
            print(b.image, b.name)
            
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
    game = BoatBattle(19,  [b1, b2], max_turn = 10)
    game.run(interactive = interactive)

