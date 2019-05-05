from UnitType import UnitType
from memutils import getMemOps


class Unit:
    def __init__(self, addr: int):
        self.addr = addr

    def getType(self):
        type = getMemOps().readInt16(self.addr + 8, 0x10)
        if type in UnitType._value2member_map_:
            return UnitType(type)
        return UnitType.OTHER

    def getHealth(self):
        return getMemOps().readFloat(self.addr + 0x30)

    def getState(self):
        type = self.getType()
        return {
            'addr': hex(self.addr),
            'type': type.value,
            'typeName': type.name,
            'health': self.getHealth(),
        }
