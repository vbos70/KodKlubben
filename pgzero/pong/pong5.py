# pong in pgzero
import random

# size of the game window
WIDTH = 800
HEIGHT = 500

# speed of players
SPEED = 2

# player 1
player1 = Actor('sprite1_magenta.png')
player1.pos = (50, HEIGHT // 2)
player1.speed_y = 0

# player2
player2 = Actor('sprite1_purple.png')
player2.pos = (WIDTH-50, HEIGHT // 2)
player2.speed_y = 0

# H is a 1/4 of the height of player 1 (could also be player 2)
H = (player1.bottom - player1.top) // 4

# ball
ball = Actor('ball_orange.png')
ball.stopped = True

def draw():    
    # a red background color mixed as RED = 128, GREEN = 0, BLUE = 0 
    screen.fill((128, 0, 0))

    # draw players
    player1.draw()
    player2.draw()

    # draw ball
    ball.draw()

def start_ball():
    ball.speed_x = random.choice([-2,2])
    
def update():
    if ball.stopped:
        ball.stopped = False
        ball.pos = (WIDTH // 2, HEIGHT // 2)
        ball.speed_x = 0
        ball.speed_y = 0
        # start the game in 3 seconds
        clock.schedule_unique(start_ball, 3)
    else:
        # Change Player 1's speed if 'w' or 'z' is pressed
        if keyboard.w:
            player1.speed_y = -SPEED
        elif keyboard.z:
            player1.speed_y = SPEED
        else:
            player1.speed_y = 0
        
        # Change Player 2's speed if 'i' or 'm' is pressed
        if keyboard.i:
            player2.speed_y = -SPEED
        elif keyboard.m:
            player2.speed_y = SPEED
            pass
        else:
            player2.speed_y = 0

        # update players and ball positions
        player1.y += player1.speed_y
        player2.y += player2.speed_y
        ball.x += ball.speed_x
        ball.y += ball.speed_y
        
        # keep players and ball on the field
        if player1.top < 0:
            player1.top = 0
        elif player1.bottom >= HEIGHT:
            player1.bottom = HEIGHT - 1

        if player2.top < 0:
            player2.top = 0
        elif player2.bottom >= HEIGHT:
            player2.bottom = HEIGHT - 1
        
        # Game stops if ball is to the left of player 1
        if ball.right < player1.left:
            ball.stopped = True
            ball.pos =  (WIDTH // 2, HEIGHT // 2)

        # Game stops if ball is to the right of player 2
        elif ball.left > player2.right:
            ball.stopped = True
            ball.pos = (WIDTH // 2, HEIGHT // 2)

        # keep ball below the top of the screen
        if ball.top <= 0:
            ball.top = 0
            ball.speed_y *= -1
        # keep ball above the bottom of the screen
        if ball.bottom >= HEIGHT - 1:
            ball.bottom = HEIGHT - 1
            ball.speed_y *= -1

        if player1.colliderect(ball):
            ball.speed_x *= -1
            if ball.y > player1.y + H:
                ball.speed_y += 1
            elif ball.y < player1.y - H:
                ball.speed_y -= 1

        # keep vertical ball speed within limits
        if ball.speed_y < -2:
            ball.speed_y = -2
        elif ball.speed_y > 2:
            ball.speed_y = 2


        
