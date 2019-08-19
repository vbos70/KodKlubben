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
class GameState:

    def __init__(self):
        self.t0 = 0

game_state = GameState()

def update( seconds,         # time since last update call
            gs = game_state  # state of the game
            ):
    print (gs.t0, seconds)
    gs.t0 += seconds

def draw():
    print ("draw called")

