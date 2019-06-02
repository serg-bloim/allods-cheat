from itertools import groupby

from Unit import Unit
from cheats import getOrCreateGame

game = getOrCreateGame()
playerA = game.getPlayerA()
print(hex(playerA))
units = game.getPlayer().getUnits()
units.sort(key=lambda u : (u.getTypeCode(),u.addr))
for u in units:
    print(u)

for (k,g) in groupby(units, Unit.getTypeCode):
    print("{0} : {1}".format(k, len(list(g))))