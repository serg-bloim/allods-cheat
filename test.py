from cheats import getOrCreateGame

player = getOrCreateGame().getPlayer()
print(player.getUnitCount())
print([hex(x.addr) for  x in player.getTCs()])