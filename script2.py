from itertools import groupby
from time import sleep

from cheats import getOrCreateGame
from gameutils import explainBuilding
from utils import *
from Unit import Unit

game = getOrCreateGame()
playerA = game.getPlayerA()
print("player : " + hex(playerA))

tc = game.getPlayer().getTCs()[0].addr
# while(True):
explainBuilding(tc)
# sleep(0.5)

