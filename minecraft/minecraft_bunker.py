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
    'height' : 4,
    'depth' : 6,
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
        print("writing configuration file: 'bunker.cfg'")
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

def bunker_space(x, y, z):
    return (x, y-1, z,
            x + bunker_width() ,
            y + bunker_height(),
            z + bunker_depth())

def clear_bunker_space(x, y, z):
    # make air space for bunker
    mc.setBlocks(x-1, y-1, z-1,
                 x + bunker_width() + 1,
                 y + 3 * bunker_height(),
                 z + bunker_depth() + 1,
                 block.AIR.id)

    # Layer of bedrock to build bunkers  
    mc.setBlocks(x-1, y-1, z-1,
                 x + bunker_width() + 1,
                 y - 1,
                 z + bunker_depth() + 1,
                 block.BEDROCK.id)
    
def build_bunker(x, y, z):
    # Create a hollow shell made of bricks.
    mc.setBlocks(x, y-1, z, x+bunker_width(), y+bunker_height(), z+bunker_depth(), block.STONE.id)
    mc.setBlocks(x+1, y, z+1, x+bunker_width()-1, y+bunker_height()-1, z+bunker_depth()-1, block.AIR.id)

    # Add doors.
    mc.setBlocks(x+2, y, z, x+2, y+1, z, block.AIR.id)
    mc.setBlocks(x+2, y, z+bunker_depth(), x+2, y+1, z+bunker_depth(), block.AIR.id)
    mc.setBlocks(x, y, z+2, x, y+1, z+2, block.AIR.id)
    mc.setBlocks(x+bunker_width(), y, z+2, x+bunker_width(), y+1, z+2, block.AIR.id)

    # Add a roof window
    mc.setBlock(x+2,y+bunker_height(),z+2, block.GLASS.id)

def clear_bunker_grid(n):
    x, y, z = bunker_pos()
    for ix in range(n):
        for iz in range(n):
            clear_bunker_space(x + bunker_width() * ix,
                               y,
                               z + bunker_depth() * iz)

def build_bunker_in_grid(ix, iz):
    x, y, z = bunker_pos()
    build_bunker(x + bunker_width() * int(ix), y, z + bunker_depth() * int(iz))

def build_all_bunkers(n):
    for ix in range(n):
        for iy in range(n):
            build_bunker_in_grid(ix, iy)
