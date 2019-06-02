from Player import Player
from UnitType import UnitType
from memutils import getMemOps


class Unit:
    def __init__(self, addr: int, player:Player):
        self.addr = addr
        self.player = player

    def getTypeCode(self):
        return getMemOps().readInt16(self.addr + 8, 0x10)

    def getType(self):
        type = self.getTypeCode()
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

    def __str__(self) -> str:
        return "{0} : {1}/{2}".format(hex(self.addr), self.getTypeCode(), self.getType().name)

