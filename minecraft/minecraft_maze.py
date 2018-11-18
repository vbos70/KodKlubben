from mcpi.minecraft import Minecraft
from mcpi import block

maze_filename = 'mymaze.txt'


maze_blocks = {
    'wall'  : block.IRON_BLOCK,
    'gap'   : block.AIR,
    'floor' : block.BEDROCK
    }

if __name__ == '__main__':
    lines = []
    with open(maze_filename, 'r') as maze_input:
        lines = maze_input.readlines()

    width = 0
    depth = 0
    for line in lines:
        depth += 1
        l = len(line)
        if l > width:
            width = l

    # Connect to Minecraft
    mc = Minecraft.create()

    # Determine the Player's current position.
    x,y,z = mc.player.getTilePos()

    mc.setBlocks(x, y-1, z,
                 x + width + 3,
                 y - 1,
                 z + depth + 3,
                 maze_blocks['floor'].id)

    mc.setBlocks(x, y, z,
                 x + width + 3,
                 y + 10,
                 z + depth + 3,
                 block.AIR.id)

    
    y0 = y
    for h in range(2):
        z0 = z + 3
        for line in lines:
            x0 = x + 3
            for c in line:
                if c == '#':
                    mc.setBlock(x0, y0 + h, z0, maze_blocks['wall'].id)

                x0 += 1
            z0 += 1

        
