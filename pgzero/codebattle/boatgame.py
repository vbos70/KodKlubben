from boatbattle import *

import animation
import pygame



################################################################################
class Bot:

    def __init__(self, name = 'Lucky'):
        self.name = name        
        self.move = Move('N', 0, 'N', 0)
        
    def step(self, game):
        moves = game.possible_moves(self)
        if len(moves)>0:
            game.execute(self, choice(moves))

            
################################################################################
class Bot1(Bot):

    def __init__(self, name = 'Braveheart'):
        super().__init__( name )

    def step(self, game):
        moves = game.possible_moves(self)

        enemy_directions = game.where_is_enemy(self)

        if game.distance_to_enemy(self) > 1:
            moves = [ m for m in moves if m.heading in enemy_directions ]
            
        smart_moves = [ m for m in moves
                        if m.fran > 0 and m.target in enemy_directions ]
        
        if len(smart_moves) > 0:
            moves = smart_moves
        if len(moves) > 0:
            m = choice(moves)
            self.move = m
            game.execute(self, self.move)

################################################################################
class Bot2(Bot):

    def __init__(self, name = 'Weasel'):
        super().__init__( name )

    def step(self, game):
        moves = game.possible_moves(self)

        enemy_directions = game.where_is_enemy(self)

        moves = [ m for m in moves if m.heading not in enemy_directions ]
            
        smart_moves = [ m for m in moves
                        if m.fran > 0 and m.target in enemy_directions ]
        
        if len(smart_moves) > 0:
            moves = smart_moves
        if len(moves) > 0:
            m = choice(moves)
            self.move = m
            game.execute(self, self.move)

################################################################################

board_size = 8
time_scale = 1.0

def load_boat_images():
    imgs = {}
    imgs["red"] =  [ Actor('ship_red_0'), Actor('ship_red_1'),  Actor('ship_red_2') ]
    imgs["blue"] = [ Actor('ship_blue_0'), Actor('ship_blue_1'), Actor('ship_blue_2') ]
    imgs["yellow"] = [ Actor('ship_yellow_0'), Actor('ship_yellow_1'), Actor('ship_yellow_2') ]
    imgs["green"] = [ Actor('ship_green_0'), Actor('ship_green_1'), Actor('ship_green_2')]
    imgs["white"] = [ Actor('ship_white_0'), Actor('ship_white_1'), Actor('ship_white_2') ]
    imgs["grey"] = [ Actor('ship_grey_0'), Actor('ship_grey_1'), Actor('ship_grey_2') ]
    return imgs

def load_explosion_images():
    imgs = [ Actor('explosion1'), Actor('explosion2'), Actor('explosion3')]
    return imgs

class BoatGame: pass

boat_game = BoatGame()

################################################################################
#
# Pick the bots you want to play: Bot, Bot1, or Bot2 (or your own)
#
################################################################################

boat_game.bot_1 = Bot1( name = 'Braveheart' )
boat_game.bot_2 = Bot2( name = 'Weasel' )

################################################################################


boat_game.boat_1_icon = Actor('ship_red_0')
boat_game.boat_2_icon = Actor('ship_yellow_0')

boat_game.boats = load_boat_images()
boat_game.explosion_imgs = load_explosion_images()
boat_game.explosions = []
boat_game.bullet_img = Actor('bullet')
boat_game.bullets = []

boat_game.boat_1_imgs = boat_game.boats["red"]
boat_game.boat_2_imgs = boat_game.boats["yellow"]

boat_game.started = False

boat_game.BB = BoatBattle(board_size, [boat_game.bot_1, boat_game.bot_2], max_turn = 1000)

CELL_SIZE = max(boat_game.boat_1_imgs[0].width, boat_game.boat_1_imgs[0].height) * 2

WIDTH  = CELL_SIZE * board_size
HEIGHT = CELL_SIZE * board_size + CELL_SIZE

def cell_coords(col_row):
    col, row = col_row
    def bc(c):
        if c < 0:
            return 0
        if c > board_size - 1:
            return board_size - 1
        return c
    
    return (bc(col) * CELL_SIZE + 0.5 * CELL_SIZE, bc(row) * CELL_SIZE + 0.5 * CELL_SIZE)


def set_boat_angle(actor, heading):
    if heading == 'N':
        actor.angle = 0
    elif heading == 'E':
        actor.angle = 90
    elif heading == 'S':
        actor.angle = 180
    elif heading == 'W':
        actor.angle = 270
    
def draw():
    screen.fill((100, 150, 200))

    for b in boat_game.bullets:
        b.draw()
        
    for e in boat_game.explosions:
        e.draw()

    set_boat_angle(boat_game.boat_1_imgs[0], boat_game.bot_1.move.heading)
    boat_game.boat_1_imgs[0].draw()

    set_boat_angle(boat_game.boat_2_imgs[0], boat_game.bot_2.move.heading)
    boat_game.boat_2_imgs[0].draw()

    # draw score board
    screen.draw.filled_rect(Rect((0,board_size * CELL_SIZE),
                                 (board_size * CELL_SIZE, CELL_SIZE)),
                            "black")
    
    screen.draw.text("Hits", midleft=(CELL_SIZE, (board_size + 0.5) * CELL_SIZE),
                     fontsize = 0.75 * CELL_SIZE
    )

    boat_game.boat_1_icon.pos = (CELL_SIZE*3, (board_size + 0.5) * CELL_SIZE)
    boat_game.boat_1_icon.draw()
    screen.draw.text("{h1}".format(h1=boat_game.BB.hits[boat_game.bot_1]),
                     center = (CELL_SIZE * 3.5, (board_size + 0.5) * CELL_SIZE),
                     fontsize = 0.75 * CELL_SIZE
    )
    screen.draw.text("{name1}".format(name1=boat_game.bot_1.name),
                     midbottom = (CELL_SIZE * 3.25, (board_size + 1) * CELL_SIZE),
                     fontsize = 0.25 * CELL_SIZE
    )
    boat_game.boat_2_icon.pos = (CELL_SIZE*5, (board_size + 0.5) * CELL_SIZE)
    boat_game.boat_2_icon.draw()
    screen.draw.text("{h2}".format(h2=boat_game.BB.hits[boat_game.bot_2]),
                     center = (CELL_SIZE * 5.5, (board_size + 0.5) * CELL_SIZE),
                     fontsize = 0.75 * CELL_SIZE
    )
    screen.draw.text("{name2}".format(name2=boat_game.bot_2.name),
                     midbottom = (CELL_SIZE * 5.25, (board_size + 1) * CELL_SIZE),
                     fontsize = 0.25 * CELL_SIZE
    )
    
def new_explosion(bullet, game_bullets):
    game_bullets.remove(bullet)
    e = animation.Animation(boat_game.explosion_imgs, bullet.pos, 0.2)
    e.start()
    boat_game.explosions.append(e)
    
def do_game_turn():
    bb = boat_game.BB
    if not bb.stop_game:
        if bb.max_turn ==  0 or bb.max_turn > bb.turn:
            bb.play_turn()

            if boat_game.bot_1.move.fran > 0:
                bullet = Actor('bullet')
                bullet.pos = cell_coords(boat_game.BB.old_position[boat_game.bot_1])
                boat_game.bullets.append(bullet)
                animate(bullet,
                        pos = cell_coords(boat_game.bot_1.tx_ty),
                        duration=time_scale / 5.0,
                        on_finished = lambda bs=boat_game.bullets, b=bullet : new_explosion(b, bs) 
                )
                boat_game.bot_1.move.fran = 0

            if boat_game.bot_2.move.fran > 0:
                bullet = Actor('bullet')
                bullet.pos = cell_coords(boat_game.BB.old_position[boat_game.bot_2])
                boat_game.bullets.append(bullet)
                animate(bullet,
                        pos = cell_coords(boat_game.bot_2.tx_ty),
                        duration=0.2,
                        on_finished = lambda bs=boat_game.bullets, b=bullet : new_explosion(b, bs)
                )
                boat_game.bot_1.move.fran = 0
            if boat_game.bot_1.move.dist > 0:
                animate(boat_game.boat_1_imgs[0],
                        pos=cell_coords(boat_game.BB.position[boat_game.bot_1]),
                        duration=time_scale
                )
                boat_game.bot_1.move.dist = 0
                
            if boat_game.bot_2.move.dist > 0:
                animate(boat_game.boat_2_imgs[0],
                        pos=cell_coords(boat_game.BB.position[boat_game.bot_2]),
                        duration=time_scale                    
                )

                boat_game.bot_2.move.dist = 0
            
        else:
            bb.stop_game = True

    
def update():
    if boat_game.BB.stop_game:
        clock.unschedule(do_game_turn)
    else:
        if not boat_game.started:
            boat_game.boat_1_imgs[0].pos = cell_coords(boat_game.BB.position[boat_game.bot_1])
            boat_game.boat_2_imgs[0].pos = cell_coords(boat_game.BB.position[boat_game.bot_2])
            boat_game.started = True
            clock.schedule_interval(do_game_turn, time_scale)

    # filter live (running) explosions
    boat_game.explosions = [ e for e in boat_game.explosions if e.running() ]
    for e in boat_game.explosions:
        e.update()

