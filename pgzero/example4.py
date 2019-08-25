# File: example4.py
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
        self.color = 255, 0, 0

game_state = GameState()

def draw():
    screen.fill(game_state.color)

