# pong in pgzero

WIDTH = 800
HEIGHT = 500


player1 = Actor('sprite1_magenta.png')
player1.pos = (50, HEIGHT // 2)
player2 = Actor('sprite1_purple.png')
player2.pos = (WIDTH-50, HEIGHT // 2)

def draw():
    
    # a red background color mixed as RED = 128, GREEN = 0, BLUE = 0 
    screen.fill((128, 0, 0))

    # draw players
    player1.draw()
    player2.draw()
    

    
