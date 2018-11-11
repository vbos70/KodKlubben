#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block

from time import sleep

# Connect to Minecraft
mc = Minecraft.create()

# Determine the Player's current position.
x,y,z = mc.player.getTilePos()

house_cfg = {
    'width' : 10,
    'height' : 8,
    'depth' : 15,
    'X' : x - 10 // 2,
    'Y' : y,
    'Z' : z - 15 // 2
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

def house_pos():
    return house_cfg['X'], house_cfg['Y'], house_cfg['Z']

def house_width():
    return house_cfg['width']

def house_depth():
    return house_cfg['depth']

def house_height():
    return house_cfg['height']

x, y, z = house_pos()

house_space = (x-2, y-2, z-2,
               x + house_width() + 2,
               y + house_height() + (house_width() // 2 + 1) + 2,
               z+house_depth() + 2)

px, py, pz = mc.player.getTilePos()
if (house_space[0] <= px and px <= house_space[3] and
    house_space[1] <= py and py <= house_space[4] and
    house_space[2] <= pz and pz <= house_space[5]):
    mc.player.setTilePos(x + house_width() // 2, y, z - house_height() )


# make air space for house
mc.setBlocks(house_space[0],
             house_space[1],
             house_space[2],
             house_space[3],
             house_space[4],
             house_space[5],
             block.AIR.id)
sleep(1)

# put a foundation
mc.setBlocks(x-2, y-1, z-2, x+2+house_width(), y-1, z+2+house_depth(), block.COBBLESTONE.id)
# Set the floor.
mc.setBlocks(x, y-1, z, x+house_width(), y-1, z+house_depth(), block.WOOD_PLANKS.id)

sleep(2)

# Create a hollow shell made of bricks.
mc.setBlocks(x,   y, z,   x+house_width(),   y+house_height(),   z+house_depth(),   block.SANDSTONE.id)
mc.setBlocks(x+1, y, z+1, x+house_width()-1, y+house_height()-1, z+house_depth()-1, block.AIR.id)

# Add a Door.
mc.setBlocks(x+1, y, z, x+1+2, y+3, z, block.AIR.id)
mc.setBlocks(x+1, y, z, x+1+2, y+1, z, block.DOOR_WOOD.id, 0)
mc.setBlocks(x+1, y+2, z, x+1+2, y+2, z, block.DOOR_WOOD.id, 8)


# Add Windows.
mc.setBlocks(x+5, y+1, z, x+house_width()-2, y+house_height()-2, z, block.GLASS.id)
mc.setBlocks(x+2, y+1, z+house_depth(), x+house_width()-2, y+house_height()-2, z+house_depth(), block.GLASS.id)
mc.setBlocks(x, y+1, z+2, x, y+house_height()-2, z+house_depth()-2, block.GLASS.id)
mc.setBlocks(x+house_width(), y+1, z+2, x+house_width(), y+house_height()-2, z+house_depth()-2, block.GLASS.id)

sleep(1)

# Add a Roof.
for i in range(int(house_width()/2) + 1):
    mc.setBlocks(x+i, y+house_height()+i, z, x+i, y+house_height()+i, z+house_depth(), block.STAIRS_WOOD.id, 0)
    mc.setBlocks(x+house_width()-i, y+house_height()+i, z, x+house_width()-i, y+house_height()+i, z+house_depth(), block.STAIRS_WOOD.id, 1)
    # Gable ends.
    if (int(house_width()/2) - i > 0):
        mc.setBlocks(x+1+i, y+house_height()+i, z, x+house_width()-i-1, y+house_height()+i, z, block.BRICK_BLOCK.id, 0)
        mc.setBlocks(x+1+i, y+house_height()+i, z+house_depth(), x+house_width()-i-1, y+house_height()+i, z+house_depth(), block.BRICK_BLOCK.id, 1)
        

