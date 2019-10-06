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

boat_game.boat_1 = boat_game.boats["red"][0]
boat_game.boat_2 = boat_game.boats["red"][1]

CELL_SIZE = max(boat_game.boat_1.width, boat_game.boat_1.height) * 2

WIDTH  = CELL_SIZE * board_size
HEIGHT = CELL_SIZE * board_size

def cell_coords(col, row):

    def bc(c):
        if c < 0:
            return 0
        if c > board_size - 1:
            return board_size - 1
        return c
    
    return (bc(col) * CELL_SIZE + 0.5 * CELL_SIZE, bc(row) * CELL_SIZE + 0.5 * CELL_SIZE)

print(boat_game.boat_2.width, boat_game.boat_2.height)

def draw():

    screen.fill((100, 150, 200))

    boat_game.boat_1.pos = cell_coords(0,0) 
    boat_game.boat_1.draw()
    boat_game.boat_2.pos = cell_coords(5,5)
    boat_game.boat_2.draw()
    
