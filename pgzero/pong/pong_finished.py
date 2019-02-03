# pong in pgzero

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

# player1 and player2 are vertical bars (see images):
# H is 1/4th of the player's vertical size
#
#
#  +-+____ player.top
#  | |  H
#  |p|____
#  |l|
#  |a| 2*H
#  |y|
#  |e|____
#  |r|  H
#  | |____ player.bottom
#  +-+
#
# We use H to compute where the ball hits the players and based on
# that the ball vertical ball speed is increased/decrease
#
H = (player1.bottom - player1.top) // 4

# ball
ball = Actor('ball_orange.png')
ball.pos = (WIDTH // 2, HEIGHT // 2)
ball.stopped = True
ball.speed_x = -2
ball.speed_y = 0

def draw():    
    # a red background color mixed as RED = 128, GREEN = 0, BLUE = 0 
    screen.fill((128, 0, 0))

    # draw players
    player1.draw()
    player2.draw()

    # draw ball
    ball.draw()

def start_ball():
    ball.stopped = False

def update():
    if ball.stopped:
        # start the game in 3 seconds
        clock.schedule(start_ball, 3)

    else:
        # update positions of moving actors

        # Player1
        if keyboard.w:
            # 'w' means UP
            player1.speed_y = -SPEED
        elif keyboard.z:
            # 'z' means DOWN
            player1.speed_y = SPEED
        else:
            # otherwise no movement
            player1.speed_y = 0
        
        # Player2
        if keyboard.i:
            # 'i' means UP
            player2.speed_y = -SPEED
        elif keyboard.m:
            # 'm' means DOWN
            player2.speed_y = SPEED
        else:
            # otherwise no movement
            player2.speed_y = 0

        # update player1's position
        player1.y += player1.speed_y
        if player1.top < 0:
            player1.top = 0
        if player1.bottom >= HEIGHT:
            player1.bottom = HEIGHT - 1

        # update player1's position
        player2.y += player2.speed_y
        if player2.top < 0:
            player2.top = 0
        if player2.bottom >= HEIGHT:
            player2.bottom = HEIGHT - 1
        
        # update ball position
        ball.x += ball.speed_x
        ball.y += ball.speed_y
        
        # make sure ball is on the field
        if ball.left < 0:
            # ball to the left of the field
            ball.stopped = True
            ball.pos =  (WIDTH // 2, HEIGHT // 2)

        elif ball.right > WIDTH-1:
            # ball to the right of the field
            ball.stopped = True
            ball.pos = (WIDTH // 2, HEIGHT // 2)

        if ball.top <= 0:
            # ball above the field
            ball.top = 0
            ball.speed_y *= -1
            
        if ball.bottom >= HEIGHT - 1:
            # ball below the field
            ball.bottom = HEIGHT - 1
            ball.speed_y *= -1

        if player1.colliderect(ball):
            # Player1 hits the ball!
            
            # reverse horizontal speed
            ball.speed_x *= -1

            # if player1 hits with upper / lower end, change vertical speed
            if ball.y > player1.y + H:
                # ball hits lower end of player 1
                # so increase vertical ball speed (downwards)
                ball.speed_y += 1
            elif ball.y < player1.y - H:
                # ball hits upper end of player 1
                # so decrease vertical ball speed (upwards)
                ball.speed_y -= 1

        if player2.colliderect(ball):
            # Player2 hits the ball!
            
            # reverse horizontal speed
            ball.speed_x *= -1

            # if player2 hits with upper / lower end, change vertical speed
            if ball.y > player2.y + H:
                # ball hits lower end of player 2
                # so increase vertical ball speed (downwards)
                ball.speed_y += 1
            elif ball.y < player2.y - H:
                # ball hits upper end of player 2
                # so decrease vertical ball speed (upwards)
                ball.speed_y -= 1
            
        # keep vertical speed within limits [-2,2]
        if ball.speed_y < -2:
            ball.speed_y = -2
        elif ball.speed_y > 2:
            ball.speed_y = 2


        
