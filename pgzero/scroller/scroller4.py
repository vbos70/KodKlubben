import pgzrun

# Window size
WIDTH = 800
HEIGHT = 600

# Game values stored in "circle"
circle = {
    'x' : 0,              # horizontal position (pixels)
    'y' : HEIGHT // 2,    # vertical position (pixels)
    'r' : WIDTH // 10,    # circle radius (pixels)
    'speed_x' : 200,      # horizontal speed (pixels/second)
    'speed_y' : 0,        # vertical speed (pixels/second)
}

# Press ESC to quit
def on_key_up(key):
    if key == keys.ESCAPE:
        exit()

    # UP-arrow moves circle up
    if key == keys.UP:
        circle['speed_y'] = -100

    # DOWN-arrow moves circle down
    elif key == keys.DOWN:
        circle['speed_y'] = 100

    # SPACE stops circle from moving up or down
    elif key == keys.SPACE:
        circle['speed_y'] = 0
        
# draw the current scene
def draw():
    # clear the screen
    screen.fill((0, 0, 0))

    # draw the circle
    screen.draw.circle((circle['x'], circle['y']),
                       circle['r'],
                       (255,0,0)
    )

# update the current scene (60 times per second!)
def update(dt):

    # compute new position of circle
    circle['x'] += dt * circle['speed_x']
    circle['y'] += dt * circle['speed_y']

    # if circle moves to the right of the screen, move it back
    if circle['x'] > WIDTH:
        circle['x'] = 0
    
    # if circle moves to the bottom of the screen, move it back
    if circle['y'] > HEIGHT:
        circle['y'] = 0
        
    # if circle moves to the top of the screen, move it back
    if circle['y'] < 0:
        circle['y'] = HEIGHT
        
# The last line starts pgzero:
pgzrun.go()


