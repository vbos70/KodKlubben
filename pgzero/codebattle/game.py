from random import choice

class Game:

    def __init__(self, bots):
        self.score = {}
        self.turn = 0
        self.max_turn = 0 # is >0, this sets the max number of turns to play
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

    def show_game(self):
        pass
            
    def run(self, interactive=True):
        self.stop_game = len(self.bots) == 0
        while not self.stop_game:
            self.show_game()
            if self.max_turn ==  0 or self.max_turn > self.turn:
                if interactive:
                    s = input("<Enter> for next turn")
                    if s.strip() == "":
                        self.play_turn()
                else:
                    self.play_turn()                    
            else:
                self.stop_game = True
            
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
