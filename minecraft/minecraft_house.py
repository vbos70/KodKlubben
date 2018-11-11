#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block

# Connect to Minecraft
mc = Minecraft.create()

# Determine the Player's current position.
x,y,z = mc.player.getTilePos()

house_cfg = {
    'width' : 10,
    'height' : 8,
    'depth' : 15,
    'X' : x + 5,
    'Y' : y,
    'Z' : z + 5
    }

try:
    with open('house.cfg') as cfg:
        for l in cfg.readlines():
            ws = l.split()
            if ws[0] in house_cfg:
                house_cfg[ws[0]] = int(ws[-1])
except IOError:
    with open('house.cfg', 'w') as cfg:
        for k in house_cfg:
            cfg.write('%s = %d\n' % (k, house_cfg[k]))


x, y, z = house_cfg['X'], house_cfg['Y'], house_cfg['Z']
width, height, depth = house_cfg['width'], house_cfg['height'],house_cfg['depth']

# make space for house
mc.setBlocks(x-2, y-1, z-2, x+width+2, y+height+2, z+depth+2, block.AIR.id)

# Create a hollow shell made of bricks.
mc.setBlocks(x,   y, z,   x+width,   y+height,   z+depth,   block.WOOD.id)
mc.setBlocks(x+1, y, z+1, x+width-1, y+height-1, z+depth-1, block.AIR.id)

# Set the floor.
mc.setBlocks(x-1, y-1, z-1, x+1+width, y-1, z+1+depth, block.COBBLESTONE.id)

# Add a Door.
mc.setBlocks(x+1, y, z, x+1+2, y+3, z, block.AIR.id)
mc.setBlocks(x+1, y, z, x+1+2, y+1, z, block.DOOR_WOOD.id, 0)
mc.setBlocks(x+1, y+2, z, x+1+2, y+2, z, block.DOOR_WOOD.id, 8)


# Add Windows.
mc.setBlocks(x+5, y+1, z, x+width-2, y+height-2, z, block.GLASS.id)
mc.setBlocks(x+2, y+1, z+depth, x+width-2, y+height-2, z+depth, block.GLASS.id)
mc.setBlocks(x, y+1, z+2, x, y+height-2, z+depth-2, block.GLASS.id)
mc.setBlocks(x+width, y+1, z+2, x+width, y+height-2, z+depth-2, block.GLASS.id)

# Add a Roof.
for i in range(int(width/2) + 1):
    mc.setBlocks(x+i, y+height+i, z, x+i, y+height+i, z+depth, block.STAIRS_WOOD.id, 0)
    mc.setBlocks(x+width-i, y+height+i, z, x+width-i, y+height+i, z+depth, block.STAIRS_WOOD.id, 1)
    # Gable ends.
    if (int(width/2) - i > 0):
        mc.setBlocks(x+1+i, y+height+i, z, x+width-i-1, y+height+i, z, block.BRICK_BLOCK.id, 0)
        mc.setBlocks(x+1+i, y+height+i, z+depth, x+width-i-1, y+height+i, z+depth, block.BRICK_BLOCK.id, 1)
        
