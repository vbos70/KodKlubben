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
class GameState: pass

# A game state with a list of colors and
# an index or the current color.
game_state = GameState()
game_state.colors = [ (255,0,0), (0,255,0), (0,0,255) ]
game_state.index = 0

def on_mouse_down():
    game_state.index += 1
    if game_state.index >= len(game_state.colors):
        game_state.index = 0
        
def draw():
    screen.fill(game_state.colors[game_state.index])
    

