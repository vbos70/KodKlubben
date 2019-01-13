import pgzrun
import time

# game screen size
WIDTH = 800
HEIGHT = 600

# the main character
ship = Actor('playership1_blue', midbottom = (400,550))

ship.speed = 0
DELTA_SPEED = 1
MAX_SPEED = 5

# create a class and instance to track game properties
class Game: pass
game = Game()
game.score = 0
game.cur_time = time.clock()
game.prev_time = game.cur_time

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
    screen.draw.text(
        str(game.score),
        color='white',
        midtop=(WIDTH // 2, 10),
        fontsize=70,
        shadow=(1, 1)
    )

def time_it():
    game.prev_time = game.cur_time
    game.cur_time = time.clock()
    game.period = game.cur_time - game.prev_time
    
def update():
    ship.x += ship.speed

    if ship.left > WIDTH:
        ship.right = 0
    elif ship.right < 0:
        ship.left = WIDTH
        
def on_mouse_down(pos):
    sounds.sfx_laser1.play()
    if ship.collidepoint(pos):
        game.score += 1
        set_ship_hurt()

def on_key_down(key, mod, unicode):
    if key == keys.SPACE:
        sounds.sfx_shielddown.play()
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




