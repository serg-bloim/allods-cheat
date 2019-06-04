from aoe2stats.Building import Building
from aoe2stats.UnitType import UnitType
from aoe2stats.Unit import Unit
from aoe2stats.memutils import MemUtils, getMemOps


class Stats:
    def __init__(self, addr, memOps):
        self.addr = addr
        try:
            self.memOps = memOps
        except:
            self.memOps = getMemOps()

    def getState(self):
        return {
            'wood':self.getWood(),
            'food':self.getFood(),
            'stone':self.getStone(),
            'gold':self.getGold(),
            'pop':self.getPop(),
            'popMax':self.getPopMax(),
            'popFree':self.getPopFree(),
            'unitsCreating':self.getUnitsCreating(),
            'unitsQueued':self.getUnitsQueued(),
        }

    def getWood(self):
        return self.memOps.readFloat(self.addr+4)

    def getFood(self):
        return self.memOps.readFloat(self.addr+0)

    def getStone(self):
        return self.memOps.readFloat(self.addr+8)

    def getGold(self):
        return self.memOps.readFloat(self.addr+0xC)

    def getPop(self):
        return self.memOps.readFloat(self.addr+0x2C)

    def getPopMax(self):
        return self.memOps.readFloat(self.addr+0x80)

    def getPopFree(self):
        return self.memOps.readFloat(self.addr+0x10)

    def getUnitsCreating(self):
        return self.memOps.readFloat(self.addr+0x144)

    def getUnitsQueued(self):
        return self.memOps.readFloat(self.addr+0x140)


class UnitClass(object):
    def __init__(self, addr):
        self.addr = addr

    def getIconId(self):
        return getMemOps().readInt16(self.addr+0x54)

class Player:
    def __init__(self, memOps: MemUtils, playerA: int):
        self.memOps = memOps
        self.addr = playerA
        self.unitContainerA = memOps.readInteger(playerA + 0x78)
        self.stats = Stats(memOps.readInteger(playerA + 0xA8), memOps=memOps)

    def getUnitsA(self):
        startUnitA = self.memOps.readInteger(self.unitContainerA + 4)
        return [self.memOps.readInteger(startUnitA + i * 4) for i in range(0, self.getUnitCount())]

    def getUnitCount(self):
        return self.memOps.readInteger(self.unitContainerA + 8)

    def getTCs(self) -> [Building]:
        return [Building(u.addr, self) for u in self.getUnits() if u.getType() == UnitType.TC]

    def getUnits(self) -> [Unit]:
        return [Unit(ua, self) for ua in self.getUnitsA()]

    def getUserType(self, ind):
        return UnitClass(self.memOps.readInteger(self.addr + 0x74, ind*4))

    def getUnitClass(self, id) -> UnitClass:
        return UnitClass(self.memOps.readInteger(self.addr + 0x78, 4*id))

    def getStats(self) -> Stats:
        return self.stats
