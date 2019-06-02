from itertools import groupby
from time import sleep

import memutils
from cheats import getOrCreateGame
from gameutils import explainBuilding
from memutils import getMemOps
from utils import *
from Unit import Unit

g = getOrCreateGame()
memutils.debug_enable = True
print(g.memeOps.readFloat(0x7912A0, 0x424, 0, 0xA8, 0x2C))