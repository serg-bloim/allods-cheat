from ctypes import c_int16

import psutil

from memutils import openProc, MemUtils


def connectGame(pid):
    return Game(openProc(pid))


def findPid():
    for proc in psutil.process_iter():
        if proc.name().lower() == 'wk.exe':
            return proc.pid
    return 0


class Game:
    handle = 0

    def __init__(self, handle):
        self.handle = handle
        self.memeOps = MemUtils(handle)

    def isValid(self):
        return self.handle > 0

    def getState(self):
        return {
            'tcs': self.getTCs()
        }

    def getTCs(self):
        return [tc for tc in self.getTCsA()]

    def getTCsA(self):
        self.getPlayerA()

    def getPlayerA(self):
        gameA = self.memeOps.pointers(0x7912A0, 0x424,0)
        print(hex(gameA))
        pInd = self.memeOps.readByPointer(c_int16, gameA + 0x94)

        return gameA


def getOrCreateGame() -> Game:
    global game
    try:
        return game
    except NameError:
        game = connectGame(findPid())
    return game
