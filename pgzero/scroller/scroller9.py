import pgzrun
from gameobject import GameObject

# Window size
WIDTH = 800
HEIGHT = 600

# Game values stored in "circle"

circle = GameObject(
    color = (255,0,0),  # Red
    x = WIDTH // 2,     # horizontal position (pixels)
    y = HEIGHT // 2,    # vertical position (pixels)
    r = WIDTH // 20,    # circle radius (pixels)
    speed_x = 0,        # horizontal speed (pixels/second)
    speed_y = 0,        # vertical speed (pixels/second)
    move_speed = 200,   # speed to move up or down
)


# The square object
square = GameObject(
    color = (0,0,255),  # Blue
    x = WIDTH,          # horizontal position (pixels)
    y = HEIGHT // 2,    # vertical position (pixels)
    s = WIDTH // 40,    # half the edge size of the square (pixels)
    speed_x = -200,     # horizontal speed (pixels/second)
    speed_y = 0,        # vertical speed (pixels/second)
    )

# The background
background = GameObject(
    num_bars = 5,             # number of vertical bars
    offset = 0,               # horizontal shift.
    speed = -50,              # speed of horizontal shift (speed of background scrolling)
    colors = [(240,220,220),  # sequence of colors for background bars
              (230,230,255),
              (230,255,230),
    ]
    )

# Game control
control = GameObject(
    pause = False,
    score = 0,
)

# Press and hold arrow up/down to move up and down 
def on_key_down(key):
    # UP-arrow moves circle up
    if key == keys.UP:
        circle.speed_y = -circle.move_speed

    # DOWN-arrow moves circle down
    elif key == keys.DOWN:
        circle.speed_y = circle.move_speed

    # RIGHT-arrow increases circle x-speed
    elif key == keys.RIGHT:
        circle.speed_x += 3
        if circle.speed_x > 500:
            circle.speed_x = 500

    # LEFT-arrow decreases circle x-speed
    elif key == keys.LEFT:
        circle.speed_x -= 3
        if circle.speed_x < 0:
            circle.speed_x = 0

    # SPACE key pauses the game
    elif key == keys.SPACE:
        control.pause = not control.pause
        
# Press ESC to quit
def on_key_up(key):
    if key == keys.ESCAPE:
        exit()

    # UP-arrow moves circle up
    if key == keys.UP:
        circle.speed_y = 0

    # DOWN-arrow moves circle down
    elif key == keys.DOWN:
        circle.speed_y = 0


# Draw the vertical bars of the background.
def draw_background():
    bar_width = WIDTH // background.num_bars
    num_fat_bars = WIDTH % background.num_bars
    num_colors = len(background.colors)

    
    def X(i):
        return i * bar_width + min(i, num_fat_bars)

    
    def W(i):
        w = bar_width
        if i < num_fat_bars:
            w += 1
        return w


    def color(i):
        return background.colors[i % num_colors]

    
    def split(x, w):
        if x+w > WIDTH:
            v = WIDTH - x
            return [(x, v+1), (0, w-v)]
        return [(x, w)]


    for b in range(background.num_bars):
        bs = split((X(b) + background.offset) % WIDTH, W(b))
        for x,w in bs:
            screen.draw.filled_rect(Rect(x, 0, w, HEIGHT), color(b))

    
# draw the current scene
def draw():
    # clear the screen
    screen.clear()

    # Draw the background
    draw_background()

    # draw the score
    screen.draw.text("Hits: {score}".format(score = control.score),
                     midtop = (WIDTH // 2, 10),
                     fontsize = 0.1 * HEIGHT,
                     color = circle.color
                     )
    
    # draw the circle
    screen.draw.circle((circle.x, circle.y),
                       circle.r,
                       circle.color
    )

    # draw the square
    s = square.s
    r = Rect((square.x-s, square.y-s), (2*s, 2*s))
    screen.draw.rect(r, square.color)

# update the current scene (60 times per second!)
def update(dt):

    if control.pause:
        return
    
    # move the background
    background.offset += dt * (background.speed - circle.speed_x)
    if background.offset > WIDTH:
        background.offset = 0
    if background.offset < 0:
        background.offset = WIDTH
        
    # compute new position of circle
    circle.y += dt * circle.speed_y

    # if circle moves to the left of the screen, move it back
    if circle.x < 0:
        circle.x = WIDTH
    
    # if circle moves to the right of the screen, move it back
    if circle.x > WIDTH:
        circle.x = 0
    
    # if circle moves to the bottom of the screen, move it back
    if circle.y > HEIGHT:
        circle.y = 0
        
    # if circle moves to the top of the screen, move it back
    if circle.y < 0:
        circle.y = HEIGHT

    # compute new position of the square
    square.x += dt * (square.speed_x - circle.speed_x)
    square.y += dt * square.speed_y

    # if square moves to the left of the screen, move it back
    if square.x < 0:
        square.x = WIDTH

    # if square moves to the right of the screen, move it back
    if square.x > WIDTH:
        square.x = 0
    
    # if square moves to the top of the screen, move it back
    if square.y < 0:
        square.y = HEIGHT
        
    # if square moves to the bottom of the screen, move it back
    if square.y > HEIGHT:
        square.y = 0

    # detect collisions by comparing the distance of the center points
    # to the size of the circle and square
    dx = (circle.x - square.x)**2
    dy = (circle.y - square.y)**2
    if (circle.r + square.s)**2 > dx + dy:
        # collision
        control.score += 1
        circle.x = WIDTH // 2
        square.x = WIDTH
                
# The last line starts pgzero:
pgzrun.go()


