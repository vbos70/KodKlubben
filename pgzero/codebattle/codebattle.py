from random import choice
from game import *

class MuminGame(Game):

    def __init__(self, max_turn, max_score, bots):
        self.max_turn = max_turn
        self.max_score = max_score
        super().__init__(bots)

    def possible_moves(self, bot):
        return ["good", "bad" ] + ([ "noop" ] * 5)
    
    def execute(self, bot, move):
        print(bot.image, "plays:", move)
        if move == "good":
            self.score[bot] = self.score[bot] + 2
        elif move == "bad" and self.score[bot] > 0:
            self.score[bot] = self.score[bot] - 1
        if self.score[bot] >= self.max_score:
            self.stop_game = True
        if self.turn >= self.max_turn:
            self.stop_game = True

    ######################################################################
    #
    # The following functions shall not be used by Bots
    #
    ######################################################################
            
    def print_score(self):
        for bot in self.bots:
            print(bot.image, bot.name, "score:", self.score[bot])
            
    def run(self):
        self.stop_game = len(self.bots) == 0
        while not self.stop_game:
            print("Turn:", self.turn)
            self.print_score()
            self.play_turn()
            print()
            
        print("Game over")
        self.print_score()

    def winners(self):
        ws = []
        if len(self.bots)>0:
            max_score = max([s for s in self.score.values()])
            ws = [ bot for bot in self.bots if self.score[bot] == max_score ]
        return ws
    
###########################################################################
#
# The Mumin bots.
#
###########################################################################
class Mumintroll(Bot):

    def initialize(self, game):
        self.name = "Mumintroll"
        self.image = "#"

class Stinky(Bot):

    def initialize(self, game):
        self.name = "Stinky"
        self.image = ">"

        
if __name__ == '__main__':

    game = MuminGame(1000, 50, [Mumintroll(), Stinky()])
    game.run()
    print()
    ws = game.winners()
    if len(ws)>0:
        if len(ws)>1:
            print("The winners are:")
        else:
            print("The winner is:")
        for w in ws:
            print(w.image, w.name)
    else:
        print("No winner(s)")
