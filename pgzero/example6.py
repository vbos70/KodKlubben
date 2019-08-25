# File: example6.py
#
# Set the window size:
WIDTH = 800
HEIGHT = 400

# To run the example6.py (pgzero) game:
#
#   terminal: pgzrun example6.py
#
# From the Mu editor:
#   Click "Play" button or hit F5

# Create a game state class
class GameState:

    def __init__(self):
        self.colors = [ (255,0,0), (0, 255, 0), (0, 0, 255) ]
        self.index = 0

game_state = GameState()

def on_mouse_down():
    game_state.index += 1
    if game_state.index >= len(game_state.colors):
        game_state.index = 0
        
def draw():
    screen.fill(game_state.colors[game_state.index])
    

