from mcpi import block
import re

# dict from block names to mcpi.block objects
mc_blocks = { n: eval('block.{}'.format(n)) for n in dir(block) if re.match('[A-Z_]+$', n) }

def mc_blocknames(_blocknames=[]):
    return [n for n in _mc_blocks.keys()]

if __name__ == '__main__':
    for n in mc_blocks:
        print(n, ':', mc_blocks[n])