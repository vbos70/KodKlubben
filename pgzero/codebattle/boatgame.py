from boatbattle import *

board_size = 10

def load_boat_images():
    imgs = {}
    imgs["red"] =  [ Actor('ship_red_0'), Actor('ship_red_1'),  Actor('ship_red_2') ]
    imgs["blue"] = [ Actor('ship_blue_0'), Actor('ship_blue_1'), Actor('ship_blue_2') ]
    imgs["yellow"] = [ Actor('ship_yellow_0'), Actor('ship_yellow_1'), Actor('ship_yellow_2') ]
    imgs["green"] = [ Actor('ship_green_0'), Actor('ship_green_1'), Actor('ship_green_2')]
    imgs["white"] = [ Actor('ship_white_0'), Actor('ship_white_1'), Actor('ship_white_2') ]
    imgs["grey"] = [ Actor('ship_grey_0'), Actor('ship_grey_1'), Actor('ship_grey_2') ]
    return imgs

class BoatGame: pass

boat_game = BoatGame()
boat_game.boats = load_boat_images()

boat_game.boat_1_imgs = boat_game.boats["red"]
boat_game.boat_2_imgs = boat_game.boats["yellow"]

boat_game.bot_1 = Bot()
boat_game.bot_2 = Bot()

boat_game.started = False

boat_game.BB = BoatBattle(board_size, [boat_game.bot_1, boat_game.bot_2], max_turn = 1000)

CELL_SIZE = max(boat_game.boat_1_imgs[0].width, boat_game.boat_1_imgs[0].height) * 2

WIDTH  = CELL_SIZE * board_size
HEIGHT = CELL_SIZE * board_size

def cell_coords(col_row):
    col, row = col_row
    def bc(c):
        if c < 0:
            return 0
        if c > board_size - 1:
            return board_size - 1
        return c
    
    return (bc(col) * CELL_SIZE + 0.5 * CELL_SIZE, bc(row) * CELL_SIZE + 0.5 * CELL_SIZE)


def draw():

    screen.fill((100, 150, 200))

    boat_game.boat_1_imgs[0].draw()
    boat_game.boat_2_imgs[0].draw()


def do_game_turn():
    print("turn", boat_game.BB.turn)
    bb = boat_game.BB
    if not bb.stop_game:
        if bb.max_turn ==  0 or bb.max_turn > bb.turn:
            bb.play_turn()
            animate(boat_game.boat_1_imgs[0], pos=cell_coords(boat_game.BB.position[boat_game.bot_1]))
            animate(boat_game.boat_2_imgs[0], pos=cell_coords(boat_game.BB.position[boat_game.bot_2]))
            
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
            clock.schedule_interval(do_game_turn, 1)
