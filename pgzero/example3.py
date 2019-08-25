# File: example3.py
#
# Set the window size:
WIDTH = 800
HEIGHT = 400

# To run the example1.py (pgzero) game:
#
#   terminal: pgzrun example1.py
#
# From the Mu editor:
#   Click "Play" button or hit F5

# Create a game state class
class GameState: pass

# A game state with a clock starting at 0 (t0)
# and ending at 5 (t1)
game_state = GameState()
game_state.t0 = 0
game_state.t1 = 5

def update( seconds         # time since last update call
            ):
    print (game_state.t0, seconds)
    if game_state.t0 > game_state.t1:
        exit()
    game_state.t0 += seconds
        
def draw():
    print ("draw called")

