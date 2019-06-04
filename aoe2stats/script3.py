import aoe2stats.memutils
from aoe2stats.cheats import getOrCreateGame

g = getOrCreateGame()
memutils.debug_enable = True
print(g.memeOps.readFloat(0x7912A0, 0x424, 0, 0xA8, 0x2C))