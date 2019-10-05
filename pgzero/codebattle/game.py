from random import choice

class Game:

    def __init__(self, bots):
        self.score = {}
        self.turn = 0
        self.bots = bots
        self.stop_game = len(self.bots) == 0
        self.init_bots()

    def possible_moves(self, bot):
        return []
    
    def execute(self, bot, move):
        pass
    
    ######################################################################
    #
    # The following functions shall not be used by Bots
    #
    ######################################################################
    def init_bots(self):
        for b in self.bots:
            self.score[b] = 0
            b.initialize(self)
            
    def play_turn(self):
        for bot in self.bots:
            bot.step(self)
        self.turn = self.turn + 1

    def run(self):
        self.stop_game = len(self.bots) == 0
        while not self.stop_game:
            print("Turn:", self.turn)
            self.play_turn()
            print()
            
        print("Game over")

    
###########################################################################
#
# The Bot base class. It randomly picks a move, if possible.
#
###########################################################################
class Bot:

    def __init__(self):
        self.name = '<noname>'
        self.image = ' '
        
    def initialize(self, game):
        pass

    def step(self, game):
        moves = game.possible_moves(self)
        if len(moves)>0:
            game.execute(self, choice(moves))
