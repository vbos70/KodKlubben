import pgzrun

# game screen size
WIDTH = 400
HEIGHT = 300

# the main character
alien = Actor('alien')   # refers to images/alien.png
alien.topright = 0, 70   # refers to tp right corner of the alien image

def draw():
    screen.fill((128, 128, 200))
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0
        alien.top += 70
        if alien.top > HEIGHT:
            alien.top = 70

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()

# put all logic to hurt the alien in one function.
# also make it automatically normal again after 1 second.
def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    alien.bottom += 20
    
    # after 1 second, call the function to make the alien normal again
    clock.schedule_unique(set_alien_normal, 1.0)
    
# this function changes the alien's image into the normal, not hurt, alien.
def set_alien_normal():
    alien.image = 'alien'
    
pgzrun.go()

# 1. How to keep track of the score (number of hits)?
# 2. How to print the score on the screen?
# 3. How to increase the alien's speed each time it starts from the top again?

