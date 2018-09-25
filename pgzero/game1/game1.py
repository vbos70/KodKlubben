# Load pygame zero
import pgzrun

# Define the game screen size
WIDTH = 400   # horizontal size
HEIGHT = 300  # vertical size

# Screen Y-coordinates start with 0 at the top. The
# largest Y-coordinate (here 300) is at the bottom of the screen.
#
# (0,0) +--------------------+
#       |                    |
#       |                    |
#       |                    |        
#       |                    |
#       |                    |
#       |                    |
#       +--------------------+ (400, 300)
        
# Create main game character (look in the images/ directory!)
alien = Actor('alien')   # refers to images/alien.png
alien.topright = 0, 70   # refers to tp right corner of the alien image

# Clear and draw the screen
def draw():
    
    # draw background color in (RED, GREEN, BLUE) values:
    screen.fill((128, 128, 160))
    
    # draw main game character:
    alien.draw()

# Perform a step of the game: update the position of the main game character.
def update():
    
    # alien.left is the alien's leftmost edge. Here it is increased by 2.
    alien.left = alien.left +  2
    
    # instead of changing the left side, you can also change the right side:
    #alien.right = alien.right + 2
    
    # Restart the alien at the left of the screen once
    # it is not visible anymore.
    if alien.left > WIDTH:
        alien.right = 0
        
        # the top of the alien is alien.top. It is increased by 70:
        alien.top += 70   # this means alien.top = alien.top + 70
        
        # Restart the alien at the top of the screen once
        # it is not visible anymore.
        if alien.top > HEIGHT:
            alien.top = 70

# Interaction with the user. Do something when the mouse is clicked.
def on_mouse_down(pos):
    
    # check if the mouse click was at the alien
    if alien.collidepoint(pos):
        
        # yes, it was, so play an "eep" sound
        sounds.eep.play()
        
        # and change the alien into a hurt alien (see images/ directory)
        alien.image = 'alien_hurt'
        
        # and make the alien drop down a bit
        alien.bottom += 20
        
    else:
        print('Ha ha, you missed!')

# start the game
pgzrun.go()



# 1. How to change the hurt alien's image back into the normal one?
# 2. In the draw function. what happens if the alien is drawn first and
#    then the background of the screen?
# 3. In the update function, what happens if you update both
#    alien.left and alien.right?