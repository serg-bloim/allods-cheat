from Building import Building
from UnitType import UnitType
from Unit import Unit
from memutils import MemUtils


class Player:
    def __init__(self, memOps: MemUtils, playerA: int):
        self.memOps = memOps
        self.addr = playerA
        self.unitContainerA = memOps.readInteger(playerA + 0x78)

    def getUnitsA(self):
        startUnitA = self.memOps.readInteger(self.unitContainerA + 4)
        return [self.memOps.readInteger(startUnitA + i * 4) for i in range(0, self.getUnitCount())]

    def getUnitCount(self):
        return self.memOps.readInteger(self.unitContainerA + 8)

    def getTCs(self) -> [Building]:
        return [Building(u.addr) for u in self.getUnits() if u.getType() == UnitType.TC]

    def getUnits(self) -> [Unit]:
        return [Unit(ua) for ua in self.getUnitsA()]
