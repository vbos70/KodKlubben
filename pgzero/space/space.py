import pgzrun
import random

# game screen size
WIDTH = 800
HEIGHT = 600

# the main character
ship = Actor('playership1_blue', midbottom = (400,550))

ship.speed = 0
DELTA_SPEED = 1
MAX_SPEED = 5

def fire_missile():
    x, y = ship.midtop
    m = Actor('laserred01.png', midbottom = (x, y+2))
    return m

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
game.active_meteors = []

def increase_speed():
    ship.speed += DELTA_SPEED
    if ship.speed > MAX_SPEED:
        ship.speed = MAX_SPEED
        
def decrease_speed():
    ship.speed -= DELTA_SPEED
    if ship.speed < -MAX_SPEED:
        ship.speed = -MAX_SPEED
        
def draw():
    screen.blit('space1_background.png', (0,0))
    #screen.fill((128, 128, 222))
    ship.draw()

    for m in game.active_meteors:
        m.draw()
        
    for m in game.missiles:
        m.draw()
    
    screen.draw.text(
        str(game.score),
        color='white',
        midtop=(WIDTH // 2, 10),
        fontsize=70,
        shadow=(1, 1)
    )

def update():

    # check if a new meteor should be added.
    if random.random() > 0.995:
        if len(game.meteors) > 0:
            m = random.choice(game.meteors)
            m.midleft = (WIDTH, random.randrange(100,400))
            m.speed_x = random.choice([-2,-3,-4])
            m.speed_y = 0
            m.rotation_speed = random.choice(range(-5,5))
            game.meteors.remove(m)
            game.active_meteors.append(m)

    # move active meteors and change their speed
    for m in game.active_meteors:
        m.x += m.speed_x
        r = random.random()
        if m.speed_y < 3 and r < 0.1:
            m.speed_y += 1
        elif m.speed_y > -3 and r > 0.9:
            m.speed_y -= 1
        
        m.y += m.speed_y
        m.angle += m.rotation_speed

        if m.right < 0:
            game.meteors.append(m)
            game.active_meteors.remove(m)

    # move the ship
    ship.x += ship.speed

    if ship.left > WIDTH:
        ship.right = 0
    elif ship.right < 0:
        ship.left = WIDTH

    # move the fired missiles
    for m in game.missiles:
        m.y -= 5
        if m.top < 15:
            game.missiles.remove(m)
            
def on_mouse_down(pos):
    sounds.sfx_laser1.play()
    if ship.collidepoint(pos):
        game.score += 1
        set_ship_hurt()

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
    ship.image = 'playership1_orange'
    ship.bottom = 570
    if ship.speed < 0.0:
        increase_speed()
    elif ship.speed > 0.0:
        decrease_speed()
    clock.schedule_unique(set_ship_normal, 2.0)
    
def set_ship_normal():
    ship.image = 'playership1_blue'
    ship.bottom = 550
    sounds.sfx_shieldup.play()
    
pgzrun.go()




