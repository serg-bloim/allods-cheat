import json

from aoe2stats.cheats import getOrCreateGame

print('player: ' + hex(getOrCreateGame().getPlayer().addr))
print(json.dumps(getOrCreateGame().getState(), indent=2))
