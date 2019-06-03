from cheats import getOrCreateGame

print('player: ' + hex(getOrCreateGame().getPlayer().addr))
print(getOrCreateGame().getState())