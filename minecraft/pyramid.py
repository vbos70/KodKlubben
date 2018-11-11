from mcpi.minecraft import Minecraft
from mcpi import block

# Connect to Minecraft
mc = Minecraft.create()

# Determine the Player's current position.
x,y,z = mc.player.getTilePos()

mc.camera.setPos(x, y+100, z)

PYRAMID_SIZE = 5
PYRAMID_BLOCK1 = block.STONE
PYRAMID_BLOCK2 = block.GLOWSTONE_BLOCK
OFFSET = 5

# Create empy space to build the pyramid
mc.setBlocks(x-PYRAMID_SIZE-OFFSET, y, z,
             x+PYRAMID_SIZE+OFFSET, y+PYRAMID_SIZE+OFFSET, + z+2*PYRAMID_SIZE+OFFSET,
             block.AIR.id)

d = 0
s = PYRAMID_BLOCK1

for layer in range(PYRAMID_SIZE):
    mc.setBlocks(x-PYRAMID_SIZE+d, y+layer, z+OFFSET+d,
                 x+PYRAMID_SIZE-d, y+layer, z+OFFSET+(2*PYRAMID_SIZE - d),
                 s.id)
    d += 1
    if s == PYRAMID_BLOCK1:
        s = PYRAMID_BLOCK2
    else:
        s = PYRAMID_BLOCK1

mc.player.setPos(x, PYRAMID_SIZE+1, PYRAMID_SIZE+OFFSET)

