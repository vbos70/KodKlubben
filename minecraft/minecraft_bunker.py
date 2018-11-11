#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block

from time import sleep

# Connect to Minecraft
mc = Minecraft.create()

# Determine the Player's current position.
x,y,z = mc.player.getTilePos()

bunker_cfg = {
    'width' : 5,
    'height' : 3,
    'depth' : 5,
    'X' : x - 5 // 2,
    'Y' : y,
    'Z' : z - 5 // 2
    }

try:
    with open('bunker.cfg') as cfg:
        for l in cfg.readlines():
            ws = l.split()
            if ws[0] in bunker_cfg:
                bunker_cfg[ws[0]] = int(ws[-1])
except IOError:
    with open('bunker.cfg', 'w') as cfg:
        for k in bunker_cfg:
            cfg.write('%s = %d\n' % (k, bunker_cfg[k]))

def bunker_pos():
    return bunker_cfg['X'], bunker_cfg['Y'], bunker_cfg['Z']

def bunker_width():
    return bunker_cfg['width'] - 1

def bunker_depth():
    return bunker_cfg['depth'] - 1

def bunker_height():
    return bunker_cfg['height'] - 1

x, y, z = bunker_pos()

bunker_space = (x, y-1, z,
                x + bunker_width() ,
                y + bunker_height(),
                z + bunker_depth())

px, py, pz = mc.player.getTilePos()
if (bunker_space[0] <= px and px <= bunker_space[3] and
    bunker_space[1] <= py and py <= bunker_space[4] and
    bunker_space[2] <= pz and pz <= bunker_space[5]):
    mc.player.setTilePos(x + bunker_width() // 2, y, z - bunker_height() )


# make air space for bunker
mc.setBlocks(bunker_space[0],
             bunker_space[1],
             bunker_space[2],
             bunker_space[3],
             bunker_space[4],
             bunker_space[5],
             block.AIR.id)
sleep(1)

# Create a hollow shell made of bricks.
mc.setBlocks(x, y-1, z, x+bunker_width(), y+bunker_height(), z+bunker_depth(), block.STONE.id)
mc.setBlocks(x+1, y, z+1, x+bunker_width()-1, y+bunker_height()-1, z+bunker_depth()-1, block.AIR.id)

# Add a Door.
mc.setBlocks(x+2, y, z, x+2, y+1, z, block.AIR.id)

# Add a roof window
mc.setBlock(x+2,y+bunker_height(),z+2, block.GLASS.id)
