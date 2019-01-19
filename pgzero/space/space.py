import pgzrun
import random
import animation

# game screen size
WIDTH = 800
HEIGHT = 600

# create a class and instance to track game properties
class Game: pass
game = Game()
game.score = 0
game.missiles = []
game.meteors = [
    Actor('meteorbrown_big1'),
    Actor('meteorbrown_big2'),
    Actor('meteorbrown_med1'),
    Actor('meteorbrown_small2'),
    Actor('meteorgrey_big1'),
    Actor('meteorgrey_big2'),
    Actor('meteorgrey_med1'),
    Actor('meteorgrey_small2'),
]
game.background = [Actor('space1_background.png'),
                   Actor('space1_background.png')]

# the main character
game.ship = Actor('playership1_blue', midbottom = (400,550))

game.ship.speed = 0
DELTA_SPEED = 1
MAX_SPEED = 5

# a flag to indicate if the ship is hit
game.ship.is_hurt = False

def fire_missile():
    x, y = game.ship.midtop
    m = Actor('laserred01.png', midbottom = (x, y+2))
    return m


# explosion image series
expl6s = [ Actor('expl_06_{:04d}.png'.format(d)) for d in range(0,25) ]

for m in game.meteors:
    m.points = 1
    if 'small' in m.image:
        m.points = 4
    elif 'med' in m.image:
        m.points = 2
    m.active = False
    
# explosions in the game
game.explosions = []

def increase_speed():
    game.ship.speed += DELTA_SPEED
    if game.ship.speed > MAX_SPEED:
        game.ship.speed = MAX_SPEED
        
def decrease_speed():
    game.ship.speed -= DELTA_SPEED
    if game.ship.speed < -MAX_SPEED:
        game.ship.speed = -MAX_SPEED

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

def detect_hits():
    for meteor in game.meteors:
        if meteor.active:
            for missile in game.missiles:
                if missile.colliderect(meteor):
                    game.explosions.append(
                        new_explosion(
                            missile.pos,
                            speed_x = meteor.speed_x,
                            speed_y = meteor.speed_y))
                    game.score += meteor.points
                    game.missiles.remove(missile)
                    make_meteor_inactive(meteor)

            if game.ship.colliderect(meteor):
                set_ship_hurt()
                game.score -= meteor.points
                make_meteor_inactive(meteor)
            
def draw():
    game.background[0].draw()
    
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

def update():

    detect_hits()

    game.background[0].topleft = (0,0)
    
    # check if a new meteor should be added.
    if random.random() > 0.995:
        inactive_meteors = [m for m in game.meteors if not m.active ]
        if len(inactive_meteors) > 0:
            m = random.choice(inactive_meteors)
            m.midleft = (WIDTH, random.randrange(100,400))
            m.speed_x = random.choice([-2,-3,-4])
            m.speed_y = 0
            m.rotation_speed = random.choice(range(-5,5))
            m.active = True

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
    game.ship.x += game.ship.speed

    if game.ship.left > WIDTH:
        game.ship.right = 0
    elif game.ship.right < 0:
        game.ship.left = WIDTH

    # move the fired missiles
    for m in game.missiles:
        m.y -= 5
        if m.top < 15:
            game.missiles.remove(m)

    # filter live (running) explosions
    game.explosions = [ e for e in game.explosions if e.running() ]
    # update explosions
    for e in game.explosions:
        e.update()
        
def on_key_down(key, mod, unicode):
    if key == keys.SPACE:
        sounds.sfx_shielddown.play()
        game.missiles.append(fire_missile())
        
    elif key == keys.A:
        decrease_speed()
    elif key == keys.D:
        increase_speed()
    
def set_ship_hurt():
    sounds.sfx_shielddown.play()
    game.ship.image = 'playership1_orange'
    game.ship.bottom = 570
    if game.ship.speed < 0.0:
        increase_speed()
    elif game.ship.speed > 0.0:
        decrease_speed()
    clock.schedule_unique(set_ship_normal, 2.0)
    
def set_ship_normal():
    game.ship.image = 'playership1_blue'
    game.ship.bottom = 550
    sounds.sfx_shieldup.play()
    
pgzrun.go()




