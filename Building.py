from Unit import Unit
from memutils import getMemOps


class QueueItem(object):
    pass


class Building(Unit):
    def hasQueue(self):
        return True

    def getQueue(self) -> [QueueItem]:
        mem = getMemOps()
        genSize = mem.readInt16(self.addr + 0x1C6)
        if genSize == 0:
            return []
        queue = mem.readInt(self.addr + 0x1C0)

        def generator():
            for batch in range(0, genSize):
                ba = queue + batch * 4
                type = mem.readInt16(ba)
                size = mem.readInt16(ba + 2)
                for _ in range(size):
                    yield type

        return list(generator())

    def getProdProgress(self):
        mem = getMemOps()
        queueItemA = mem.readInteger(self.addr + 0x1CC, 8, 0)
        timeCreating = mem.readFloat(queueItemA + 0x44)
        unitType = mem.readInt16(queueItemA + 0x40)
        if unitType == 0:
            return 0
        totalCreationTime = mem.readInt16(queueItemA + 8, 0xC, 0x74, 4 * unitType, 0x182)
        return timeCreating / totalCreationTime

    def getState(self):
        state = super(Building, self).getState()
        state.update({
            'queue': self.getQueue(),
            'prodProgress': self.getProdProgress()
        })
        return state