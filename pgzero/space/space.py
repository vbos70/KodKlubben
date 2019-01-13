import pgzrun

# game screen size
WIDTH = 800
HEIGHT = 600

# the main character
ship = Actor('playership1_blue')
ship.right = 0
ship.top = 400
ship.score = 0
ship.speed = 2

def draw():
    screen.fill((128, 128, 222))
    ship.draw()
    screen.draw.text(
        str(ship.score),
        color='white',
        midtop=(WIDTH // 2, 10),
        fontsize=70,
        shadow=(1, 1)
    )


def update():
    ship.left += ship.speed
    if ship.left > WIDTH:
        ship.right = 0
        ship.top += 70
        if ship.top > HEIGHT:
            ship.top = 70
            ship.speed += 1

def on_mouse_down(pos):
    sounds.sfx_laser1.play()
    if ship.collidepoint(pos):
        ship.score += 1
        set_ship_hurt()

def set_ship_hurt():
    ship.image = 'playership1_orange'
    ship.bottom += 20
    sounds.sfx_shielddown.play()
    clock.schedule_unique(set_ship_normal, 1.0)
    
def set_ship_normal():
    ship.image = 'playership1_blue'
    sounds.sfx_shieldup.play()
    
pgzrun.go()




