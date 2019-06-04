from itertools import groupby
from time import sleep

from aoe2stats.cheats import getOrCreateGame
from aoe2stats.gameutils import explainBuilding
from aoe2stats.utils import *
from aoe2stats.Unit import Unit

game = getOrCreateGame()
playerA = game.getPlayerA()
print("player : " + hex(playerA))

tc = game.getPlayer().getTCs()[0].addr
# while(True):
explainBuilding(tc)
# sleep(0.5)

