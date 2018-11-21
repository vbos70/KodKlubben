import sys
from mcpi.minecraft import Minecraft
from mcpi import block
from mcblocks import mc_blockmap

def build(filename, names):
    with open(filename, 'r') as mcbfile:
        linenum = 0
        dz = 0
        for l in mcbfile.readlines():
            linenum += 1
            if '=' in l:
                words = l.split()
                if words[1] == '=':
                    names[words[0]] = words[2]
                    if words[0] == 'y':
                        dz = 0                        
                else:
                    print('%s: Error on line %d' % (filename,linenum))
            else:
                chars = l.strip()
                if len(chars) > 0 and chars[0] != '%':
                    dx = 0
                    for c in chars:
                        if c in names:
                            b = names[c]
                        else:
                            b = 'AIR'
                        mc.setBlock(names['x0']+dx,
                                    names['y0']+int(names['y']),
                                    names['z0']+dz,
                                    mc_blockmap[b].id)
                        dx += 1
                    dz += 1
        

# Connect to Minecraft
mc = Minecraft.create()

# Determine the Player's current position.
x,y,z = mc.player.getTilePos()


for filename in sys.argv[1:]:
    print('building:', filename)
    build(filename, { 'x0' : x+1, 'y0' : y, 'z0' : z})

