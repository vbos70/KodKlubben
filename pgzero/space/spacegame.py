import pgzrun
import random
import animation
from math import sin, cos, radians

# game screen size
WIDTH = 800
HEIGHT = 600

STOPPED = 0
RUNNING = 1
PAUSED = 2
IDLE = 3
INTRO = 4

messages = {
    STOPPED : "STOPPED",
    RUNNING : None,
    PAUSED : "PAUSED",
    IDLE : "IDLE",
    INTRO : "INTRO"
    }

# create a class and instance to track game properties
class Game:
    def __init__(self):
        self.score = 0
        self.missiles = []
        self.time = 0
        self.explosions = []
        self.time = 0
        self.stopped = False
        self.stars = []
        self.state = IDLE

        # create some meteors (see images/ folder for more!)
        self.meteors = [
            Actor('meteorbrown_big1'),
            Actor('meteorbrown_big2'),
            Actor('meteorbrown_med1'),
            Actor('meteorbrown_small2'),
            Actor('meteorgrey_big1'),
            Actor('meteorgrey_big2'),
            Actor('meteorgrey_med1'),
            Actor('meteorgrey_small2'),
        ]
        for m in self.meteors:
            # assign points to the meteors
            m.points = 1
            if 'small' in m.image:
                m.points = 4
            elif 'med' in m.image:
                m.points = 2
            # and deactivate all meteors
            m.active = False

        # set the background
        self.background = Actor('space1_background.png')

        # create a space ship (see images/ folder for other ships)
        self.ship = Actor('playership1_blue', center = (WIDTH//2,HEIGHT//2))
        
game = Game()

def pause_game():
    game.state = PAUSED

def continue_game():
    game.state = RUNNING
    clock.schedule_unique(decrease_time, 1.0)
    clock.schedule_unique(new_meteor,0.5)

def rotate_ship():
    if len(game.ship.angles) > 0:
        game.ship.angle = game.ship.angles[0]
        del game.ship.angles[0]
        clock.schedule_unique(rotate_ship, 0.005)
    else:
        clock.schedule_unique(continue_game, 0.5)

def show_intro():
    game.state = INTRO
    game.ship.angles =[d for d in range(0, 360, 10)] + [0]
    game.ship.angles += [d for d in range(360, 0, -10)] + [0]
    rotate_ship()

def start_game():
    show_intro()
    game.time = 2*60
    game.score = 0
    game.explosions = []
    set_ship_normal()
    for m in game.meteors:
        m.active = False
    continue_game()

def stop_game():
    game.state = IDLE
    
def is_state(s):
    return game.state == s

def set_ship_hurt():
    game.ship.is_hurt = True
    game.ship.image = 'playership1_orange'
    game.ship.missile_loaded = False
    sounds.sfx_shielddown.play()
    clock.schedule_unique(set_ship_normal, 2.0)

def set_ship_normal():
    game.ship.is_hurt = False
    game.ship.image = 'playership1_blue'
    game.ship.missile_loaded = True
    game.ship.speed = 0
    sounds.sfx_shieldup.play()

def load_missile():
    game.ship.missile_loaded = True

def fire_missile():
    game.ship.missile_loaded = False
    h = game.ship.height / 2
    x0 = (h + 2) * sin(-radians(game.ship.angle))
    y0 = (h + 2) * cos(-radians(game.ship.angle))

    x1 = (h + 2 + 5) * sin(-radians(game.ship.angle))
    y1 = (h + 2 + 5) * cos(-radians(game.ship.angle))

    x, y = game.ship.center
    x = x + x0
    y = y - y0
    
    m = Actor('laserred01.png', angle=game.ship.angle, pos=(x,y))
    m.speed_x = x1 - x0
    m.speed_y = -(y1 - y0)
    
    m.angle = game.ship.angle

    clock.schedule(load_missile, 0.5)
    return m

# explosion image series
expl6s = [ Actor('expl_06_{:04d}.png'.format(d)) for d in range(0,25) ]

def make_meteor_active(m):
    m.active = True

def make_meteor_inactive(m):
    m.active = False

def new_explosion(pos, speed_x=0, speed_y=0):
    sounds.explosion1.play()
    e = animation.Animation(expl6s, pos, 0.05, speed_x, speed_y)
    e.start()
    game.explosions.append(e)
    return e

def new_meteor():
    if is_state(RUNNING):

        inactive_meteors = [m for m in game.meteors if not m.active ]
        if random.randrange(0, len(game.meteors)) < len(inactive_meteors):
            m = random.choice(inactive_meteors)
            m.midleft = (WIDTH, random.randrange(100,HEIGHT-200))
            m.speed_x = random.choice([-2,-3,-4])
            m.speed_y = 0
            m.rotation_speed = random.choice(range(-5,5))
            m.active = True
        clock.schedule_unique(new_meteor, 0.5)

def in_between_pos(p1, p2):
    return ((p1[0] + p2[0]) // 2,
            (p1[1] + p2[1]) // 2)

def detect_hits():
    for meteor in game.meteors:
        if meteor.active:
            for missile in game.missiles:
                if missile.colliderect(meteor):
                    game.explosions.append(
                        new_explosion(
                            in_between_pos(meteor.pos, missile.pos),
                            speed_x = meteor.speed_x,
                            speed_y = meteor.speed_y))
                    game.score += meteor.points
                    game.missiles.remove(missile)
                    make_meteor_inactive(meteor)

            if game.ship.colliderect(meteor):
                game.explosions.append(
                    new_explosion(
                        meteor.pos,
                        speed_x = meteor.speed_x,
                        speed_y = meteor.speed_y))
                set_ship_hurt()
                game.score -= meteor.points
                make_meteor_inactive(meteor)

def draw():
    screen.fill((5,10,20))
    game.background.draw()

    game.ship.draw()

    for m in game.meteors:
        if m.active:
            m.draw()

    for m in game.missiles:
        m.draw()

    for e in game.explosions:
        e.draw()

    screen.draw.text(
        str(game.score),
        color='white',
        midtop=(WIDTH // 2, 10),
        fontsize=70,
        shadow=(1, 1)
    )

    screen.draw.text(
        str(game.time),
        color='white' if game.time > 10 else 'red',
        midtop=(WIDTH - 50, 10),
        fontsize=70,
        shadow=(1, 1)
    )

    if messages[game.state] is not None:
        screen.draw.text(
            messages[game.state],
            color='yellow',
            midbottom=(WIDTH // 2, HEIGHT // 2),
            fontsize=70,
            shadow=(1, 1)
        )

def on_mouse_move(pos):
    if is_state(RUNNING):
        game.ship.angle = game.ship.angle_to(pos) - 90

def on_mouse_up(pos):
    if is_state(RUNNING):
        if(not game.ship.is_hurt) and (game.ship.missile_loaded):
            game.missiles.append(fire_missile())
    
def on_key_up(key):
    if key == keys.SPACE:
        if is_state(RUNNING):
            if(not game.ship.is_hurt) and (game.ship.missile_loaded):
                game.missiles.append(fire_missile())
        elif is_state(PAUSED):
            continue_game()
        elif is_state(IDLE):
            start_game()
            
    elif key == keys.ESCAPE:
        if is_state(RUNNING) or is_state(PAUSED):
            stop_game()
            
    
def update_actors():
    #game.ship.speed = 0

    #if keyboard.a:
    #    game.ship.speed = -2
    #elif keyboard.d:
    #    game.ship.speed = 2

    detect_hits()

    # move active meteors and change their speed
    for m in game.meteors:
        if m.active:
            r = random.random()
            if m.speed_y < 3 and r < 0.1:
                m.speed_y += 1
            elif m.speed_y > -3 and r > 0.9:
                m.speed_y -= 1

            m.x += m.speed_x
            m.y += m.speed_y
            m.angle += m.rotation_speed

            if m.right < 0:
                m.active = False

    # move the ship
    #game.ship.x += game.ship.speed

    if game.ship.left < 0:
        game.ship.left = 0
    elif game.ship.right > WIDTH-1:
        game.ship.right = WIDTH-1

    # move the fired missiles
    for m in game.missiles:
        m.x += m.speed_x
        m.y += m.speed_y
        if m.top < 0:
            game.missiles.remove(m)

    # filter live (running) explosions
    game.explosions = [ e for e in game.explosions if e.running() ]
    # update explosions
    for e in game.explosions:
        e.update()

def decrease_time():
    if is_state(RUNNING):
        game.time -= 1
        clock.schedule_unique(decrease_time, 1.0)

def update():

    if is_state(RUNNING):
        update_actors()
        if game.time < 1:
            stop_game()

def quit_game():
    exit()

pgzrun.go()
