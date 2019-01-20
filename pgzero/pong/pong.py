# pong in pgzero

WIDTH = 800
HEIGHT = 500


player1 = Actor('sprite1_magenta.png')
player1.pos = (50, HEIGHT // 2)
player1.speed_y = 0

player2 = Actor('sprite1_purple.png')
player2.pos = (WIDTH-50, HEIGHT // 2)
player2.speed_y = 0


ball = Actor('ball_orange.png')

ball.init_pos = WIDTH // 2, HEIGHT // 2
ball.pos = ball.init_pos
ball.speed_x = -2 # maybe use random number here
ball.speed_y = 0

ball.stopped = True

bh_1_4 = (ball.bottom - ball.top) // 4
bh_1_8 = (ball.bottom - ball.top) // 8

def draw():
    
    # a red background color mixed as RED = 128, GREEN = 0, BLUE = 0 
    screen.fill((128, 0, 0))

    # draw players
    player1.draw()
    player2.draw()
    
    ball.draw()


def start_ball():
    ball.stopped = False

def update():

    if ball.left < 0:
        ball.stopped = True
        ball.pos = ball.init_pos

    elif ball.right > WIDTH-1:
        ball.stopped = True
        ball.pos = ball.init_pos

    if not ball.stopped:
        ball.x += ball.speed_x
        ball.y += ball.speed_y

        if player1.colliderect(ball):
            ball.speed_x *= -1
            ball.left = player1.right + 1
            if ball.y > player1.y + bh_1_4:
                ball.speed_y += 2
            elif ball.y > player1.y + bh_1_8:
                ball.speed_y += 1
            elif ball.y < player1.y - bh_1_8:
                ball.speed_y -= 1
            elif ball.y < player1.y - bh_1_4:
                ball.speed_y -= 2

        if player2.colliderect(ball):
            ball.speed_x *= -1
            ball.right = player2.left - 1

            if ball.y > player2.y + bh_1_4:
                ball.speed_y += 2
            elif ball.y > player2.y + bh_1_8:
                ball.speed_y += 1
            elif ball.y < player2.y - bh_1_8:
                ball.speed_y -= 1
            elif ball.y < player2.y - bh_1_4:
                ball.speed_y -= 2

        # keep speed_y within [-2..2]
        if ball.speed_y < -2:
            ball.speed = -2
        elif ball.speed_y > 2:
            ball.speed_y = 2
                
        if ball.top <= 0:
            ball.top = 0
            ball.speed_y *= -1
            
        if ball.bottom >= HEIGHT - 1:
            ball.bottom = HEIGHT - 1
            ball.speed_y *= -1
            
    SPEED = 2
    if keyboard.w:
        player1.speed_y = -SPEED
    elif keyboard.z:
        player1.speed_y = SPEED
    else:
        player1.speed_y = 0
        
    if keyboard.i:
        player2.speed_y = -SPEED
    elif keyboard.m:
        player2.speed_y = SPEED
    else:
        player2.speed_y = 0

    player1.y += player1.speed_y
    if player1.top < 0:
        player1.top = 0
    if player1.bottom >= HEIGHT:
        player1.bottom = HEIGHT - 1

    player2.y += player2.speed_y
    if player2.top < 0:
        player2.top = 0
    if player2.bottom >= HEIGHT:
        player2.bottom = HEIGHT - 1

    if ball.stopped:
        clock.schedule(start_ball, 3)
        
