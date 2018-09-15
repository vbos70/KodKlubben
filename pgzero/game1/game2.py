import pgzrun

alien = Actor('alien')
alien.topright = 0, 10

WIDTH = 400
HEIGHT = 300

def draw():
    screen.fill((128, 128, 0))
    alien.draw()


def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0
        alien.top += 40
        if alien.top > HEIGHT:
            alien.top = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()

def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    alien.bottom += 20
    clock.schedule_unique(set_alien_normal, 1.0)
    
def set_alien_normal():
    alien.image = 'alien'
    
pgzrun.go()
