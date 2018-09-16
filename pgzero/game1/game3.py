import pgzrun

# game screen size
WIDTH = 400
HEIGHT = 300

# the main character
alien = Actor('alien')   # refers to images/alien.png
alien.topright = 0, 70   #
alien.score = 0
alien.speed = 2

def draw():
    screen.fill((128, 128, 200))
    alien.draw()
    screen.draw.text(
        str(alien.score),
        color='white',
        midtop=(WIDTH // 2, 10),
        fontsize=70,
        shadow=(1, 1)
    )


def update():
    alien.left += alien.speed
    if alien.left > WIDTH:
        alien.right = 0
        alien.top += 70
        if alien.top > HEIGHT:
            alien.top = 70
            alien.speed += 2

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        alien.score += 1
        set_alien_hurt()

def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    alien.bottom += 20
    clock.schedule_unique(set_alien_normal, 1.0)
    
def set_alien_normal():
    alien.image = 'alien'
    
pgzrun.go()


# 1. How to increase the speed only if the alien was hit at least once?
