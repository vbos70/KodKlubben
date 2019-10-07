from boatbattle import *

class Bot1(Bot):

    def step(self, game):
        moves = game.possible_moves(self)

        enemy_directions = game.where_is_enemy(self)

        if game.distance_to_enemy(self) > 2:
            moves = [ m for m in moves if game.move_direction(m) in enemy_directions ]
            
        smart_moves = [ m for m in moves if game.fires(m) and game.target_direction(m) in enemy_directions ]
        if len(smart_moves) > 0:
            game.execute(self, choice(smart_moves))
        else:
            game.execute(self, choice(moves))
