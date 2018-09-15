import pgzrun

alien = Actor('alien')
alien.topright = 0, 10

WIDTH = 400
HEIGHT = 300

def draw():
    screen.fill((128, 128, 0))
    alien.draw()


def update():
    alien.left = alien.left +  2
    if alien.left > WIDTH:
        alien.right = 0
        alien.top += 40
        if alien.top > HEIGHT:
            alien.top = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        sounds.eep.play()
        alien.image = 'alien_hurt'
        alien.bottom += 20
    else:
        print('Ha ha, you missed!')
    
pgzrun.go()
