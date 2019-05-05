from ctypes import *

import psutil

from UnitType import UnitType
from memutils import *


def connectGame(pid):
    return Game(openProc(pid))


def findPid():
    for proc in psutil.process_iter():
        if proc.name().lower() == 'wk.exe':
            return proc.pid
    return 0


class Unit:
    def __init__(self, addr: int):
        self.addr = addr

    def getType(self):
        return getMemOps().readInt16(self.addr + 8, 0x10)


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

    def getTCs(self):
        return [tc for tc in self.getTCsA()]

    def getTCsA(self):
        return [u for u in self.getUnits() if u.getType() == UnitType.TC]

    def getUnits(self):
        return [Unit(ua) for ua in self.getUnitsA()]


class Game:
    handle = 0

    def __init__(self, handle):
        self.handle = handle
        self.memeOps = MemUtils(handle)

    def isValid(self):
        return self.handle > 0

    def getState(self):
        return {
            'tcs': self.getPlayer().getTCs()
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


def getOrCreateGame() -> Game:
    global game
    try:
        return game
    except NameError:
        game = connectGame(findPid())
    return game
