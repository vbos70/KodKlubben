# File: example5.py
#
# Set the window size:
WIDTH = 800
HEIGHT = 400

# To run the example5.py (pgzero) game:
#
#   terminal: pgzrun example5.py
#
# From the Mu editor:
#   Click "Play" button or hit F5

# Create a game state class
class GameState:

    def __init__(self):
        self.mouse_clicks = 0

game_state = GameState()

def on_mouse_down():
    game_state.mouse_clicks += 1
    print (game_state.mouse_clicks)



