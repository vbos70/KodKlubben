import pgzrun

# Window size
WIDTH = 800
HEIGHT = 600

# Game values stored in "circle"
circle = {
    'x' : 0,              # horizontal position (pixels)
    'y' : HEIGHT // 2,    # vertical position (pixels)
    'r' : WIDTH // 10,    # circle radius (pixels)
    'speed_x' : 10,       # horizontal speed (pixels/second)
    'speed_y' : 0,        # vertical speed (pixels/second)
}

# Press ESC to quit
def on_key_up(key):
    if key == keys.ESCAPE:
        exit()

# draw the current scene
def draw():
    screen.draw.circle((circle['x'], circle['y']),
                       circle['r'],
                       (255,0,0)
    )

# update the current scene (60 times per second!)
def update(dt):
    
    # compute new position of 
    circle['x'] += dt * circle['speed_x']
    circle['y'] += dt * circle['speed_y']

# The last line starts pgzero:
pgzrun.go()


