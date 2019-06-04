from ctypes import c_int16, c_int

from aoe2stats.Player import Player
from aoe2stats.memutils import MemUtils


class Game:
    handle = 0

    def __init__(self, handle):
        self.handle = handle
        self.memeOps = MemUtils(handle)

    def isValid(self):
        return self.handle > 0

    def getState(self):
        return {
            'playerStats': self.getPlayer().getStats().getState(),
            'tcs': [ tc.getState() for tc in self.getPlayer().getTCs()]
        }


    def getAllUnitsA(self):
        def getPlayerA(self):
            gameA = self.memeOps.pointers(0x7912A0, 0x424, 0)
            print(hex(gameA))
            pInd = self.memeOps.readByPointer(c_int16, gameA + 0x94)
            return self.memeOps.readByPointer(c_int, gameA + 0x4C, 4 * pInd)

    def getPlayerA(self):
        gameA = self.memeOps.pointers(0x7912A0, 0x424, 0)
        print(hex(gameA))
        pInd = self.memeOps.readByPointer(c_int16, gameA + 0x94)
        return self.memeOps.readByPointer(c_int, gameA + 0x4C, 4 * pInd)

    def getPlayer(self) -> Player:
        return Player(self.memeOps, self.getPlayerA())