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
            
    def play_turn(self):
        for bot in self.bots:
            bot.step(self)
        self.turn = self.turn + 1

            
            
