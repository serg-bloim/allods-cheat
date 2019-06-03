import json

from cheats import getOrCreateGame

print('player: ' + hex(getOrCreateGame().getPlayer().addr))
print(json.dumps(getOrCreateGame().getState(), indent=2))
