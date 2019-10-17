from boatbattle import *

import animation
import pygame



################################################################################
class Bot:

    def __init__(self, name, icons ):
        self.name = name        
        self.move = Move('N', 0, 'N', 0)
        self.icons = icons
        self.hit = False
        
    def step(self, game):
        moves = game.possible_moves(self)
        if len(moves)>0:
            game.execute(self, choice(moves))

    def is_alive(self):
        return len(self.icons) > 0
    
################################################################################
class Bot1(Bot):

    def __init__(self, name, icons):
        super().__init__( name, icons )

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

    def __init__(self, name, icons):
        super().__init__( name, icons )

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
time_scale = 0.5

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

boat_game.bots = [
    Bot ( 'Lucky',      ['ship_green_0',  'ship_green_1',  'ship_green_2'] ),
    Bot1( 'Braveheart', ['ship_red_0',    'ship_red_1',    'ship_red_2'] ),
    Bot2( 'Weasel',     ['ship_yellow_0', 'ship_yellow_1', 'ship_yellow_2'] )
    ]

NUM_BOTS = len(boat_game.bots)

# players are moving on the board
boat_game.players = { b : [ Actor(b.icons[i]) for i in range(len(b.icons)) ]
                      for b in boat_game.bots }
          
# icons are symbols on the score board
boat_game.icons = [ Actor(b.icons[0]) for b in boat_game.bots ]

################################################################################

def player(bot):
    idx = min(len(boat_game.players[bot]), boat_game.BB.hits[bot])
    return boat_game.players[bot][idx]

boat_game.explosion_imgs = load_explosion_images()
boat_game.explosions = []
boat_game.bullet_img = Actor('bullet')
boat_game.bullets = []
boat_game.started = False
boat_game.BB = BoatBattle(board_size, boat_game.bots, max_turn = 1000)

# assume all players have the same size
p = player(boat_game.bots[0])
CELL_SIZE = max(p.width, p.height) * 2

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


def boat_angle(heading):
    if heading == 'N':
        return 180
    elif heading == 'E':
        return 90
    elif heading == 'S':
        return 0
    elif heading == 'W':
        return 270
    return 45 # should never happen !?

def draw():
    screen.fill((100, 150, 200))

    for b in boat_game.bullets:
        b.draw()
        
    for e in boat_game.explosions:
        e.draw()

    for b in boat_game.BB.alive_bots():
        a = player(b)
        a.draw()

    # draw score board
    screen.draw.filled_rect(Rect((0,board_size * CELL_SIZE),
                                 (board_size * CELL_SIZE, CELL_SIZE)),
                            "black")
    
    screen.draw.text("Hits", midleft=(CELL_SIZE/4, (board_size + 0.5) * CELL_SIZE),
                     fontsize = 0.75 * CELL_SIZE
    )
    x = CELL_SIZE*2
    for i in range(NUM_BOTS):
        bot = boat_game.bots[i]
        icon = boat_game.icons[i]
        
        icon.pos = (x, (board_size + 0.5) * CELL_SIZE)
        icon.draw()
        screen.draw.text("{hits}".format(hits=boat_game.BB.hits[bot]),
                         midleft = (x + 0.2*CELL_SIZE, (board_size + 0.5) * CELL_SIZE),
                         fontsize = 0.5 * CELL_SIZE
        )
        screen.draw.text("{name}".format(name=bot.name),
                         bottomleft = (icon.left, (board_size + 1) * CELL_SIZE),
                         fontsize = 0.25 * CELL_SIZE
        )
        x += CELL_SIZE

def new_explosion(bot, bullet, game_bullets):
    game_bullets.remove(bullet)
    if bot.hit:
        bot.hit = False
        e = animation.Animation(boat_game.explosion_imgs, bullet.pos, time_scale / 5)
        e.start()
        boat_game.explosions.append(e)

def do_game_turn():
    bb = boat_game.BB
    # game ends if all but one bot are not alive anymore
    if len([ b for b in bb.bots if bb.is_alive(b) ]) <= 1:
        bb.stop_game = True

    if not bb.stop_game:
        if bb.max_turn ==  0 or bb.max_turn > bb.turn:
            bb.play_turn()

            for b in bb.alive_bots():
                if b.move.fran > 0:
                    bullet = Actor('bullet')
                    bullet.pos = cell_coords(boat_game.BB.old_position[b])
                    boat_game.bullets.append(bullet)
                    animate(bullet,
                            pos = cell_coords(b.tx_ty),
                            duration=time_scale / 5.0,
                            on_finished = lambda bot=b, bs=boat_game.bullets, b=bullet : new_explosion(bot, b, bs) 
                    )
                    b.move.fran = 0
            for b in bb.alive_bots():
                a = player(b)
                a.angle = boat_angle(b.move.heading)
                a.pos = cell_coords(boat_game.BB.old_position[b])
                if b.move.dist > 0:
                    animate(a,
                            pos=cell_coords(boat_game.BB.position[b]),
                            duration=time_scale
                    )
                    b.move.dist = 0
                            
        else:
            bb.stop_game = True

    
def update():
    if boat_game.BB.stop_game:
        if boat_game.started:
            clock.unschedule(do_game_turn)
            print('Game over')
            boat_game.started = False
    else:
        if not boat_game.started:
            boat_game.started = True
            clock.schedule_interval(do_game_turn, time_scale)

    # filter live (running) explosions
    boat_game.explosions = [ e for e in boat_game.explosions if e.running() ]
    for e in boat_game.explosions:
        e.update()

