# File: example2.py
#
# Set the window size:
WIDTH = 800
HEIGHT = 400

# To run the example1.py (pgzero) game:
#
#   terminal: pgzrun example1.py
#
# From the Mu editor:
#   Click "Play" button or hit F5

# pgzero's main loop calls:
#
#   update()
#   draw()
#
# at a rate of more or less 60Hz (60 times per second)

def update():
    print ("update called")

def draw():
    print ("draw called")

