from enum import IntEnum, Enum

import memutils
from Unit import Unit
from memutils import getMemOps


class QueueItem(object):
    pass

class UnitKind(IntEnum):
    UNIT=1
    BUILDING=2
    TECH=3

class UnitInProd(object):
    def __init__(self, type, progress, remainingTime, iconId = -1, kind=UnitKind.UNIT):
        self.type = type
        self.progress = progress
        self.remainingTime = remainingTime
        self.iconId = iconId
        self.kind = int(kind)

    def exists(self):
        return self.type != -1


class Building(Unit):
    def hasQueue(self):
        return True

    def getQueue(self) -> [QueueItem]:
        mem = getMemOps()
        genSize = mem.readInt16(self.addr + 0x1C6)
        if genSize == 0:
            return []
        queue = mem.readInt(self.addr + 0x1C0)
        # unit_type_arr = mem.readInteger(self.player.getUnitTypeArr())
        def generator():
            for batch in range(0, genSize):
                ba = queue + batch * 4
                type = mem.readInt16(ba)
                size = mem.readInt16(ba + 2)
                iconId = self.player.getUserType(type).getIconId()
                item = UnitInProd(type, 0, 0, iconId, UnitKind.UNIT)
                for _ in range(size):
                    yield item

        return list(generator())

    def getUnitProd(self):
        mem = getMemOps()
        queueItemA = mem.readInteger(self.addr + 0x1CC, 8, 0)
        timeCreating = mem.readFloat(queueItemA + 0x44)
        unitType = mem.readInt16(queueItemA + 0x40)
        if unitType == 0:
            return 0,0
        totalCreationTime = mem.readInt16(queueItemA + 8, 0xC, 0x74, 4 * unitType, 0x182)
        return timeCreating / totalCreationTime, totalCreationTime-timeCreating

    def getState(self):
        state = super(Building, self).getState()
        queue = self.getQueue()
        progress,remainingTime = self.getUnitProd()
        techProd = self.getTechProd()
        if techProd.exists() and progress == 0 and len(queue) == 0:
            progress = techProd.progress
            remainingTime = techProd.remainingTime
            queue = [techProd]
        state.update({
            'queue': [ vars(i) for i in queue],
            'prodProgress': progress,
            'prodRemaining': remainingTime,
            'techInProd': vars(techProd),
        })
        return state

    def getTechProd(self):
        mem = getMemOps()
        memutils.debug_enable = True
        currTech = mem.readInteger(self.addr + 0x1A0, 8)
        type = -1
        progress = 0
        remainingTime = 0
        iconId = -1
        if currTech != 0:
            type = mem.readInt16(currTech, 0x40)
            unitLibrary = mem.readInteger(self.addr + 0xC, 0x12A0)
            timeCreating = mem.readFloat(unitLibrary, 0x10 * type)
            timeTotal1 = mem.readInt16(unitLibrary,  0x10 * type + 0xC)
            timeTotal2 = mem.readInt16(unitLibrary + 8, 0,  type * 0x44 + 0x26)
            iconId = mem.readInt16(unitLibrary + 8, 0,  type * 0x44 + 0x2C)
            timeTotal = timeTotal1 + timeTotal2
            progress = timeCreating / timeTotal
            remainingTime = timeTotal - timeCreating
        return UnitInProd(type=type, progress=progress, remainingTime=remainingTime, iconId = iconId, kind=UnitKind.TECH)
