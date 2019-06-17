import psutil

from aoe2stats.Game import Game
from aoe2stats.memutils import *

proc_name = 'aoe2_x1.exe'
def connectGame(pid):
    return Game(openProc(pid))


def findPid():
    for proc in psutil.process_iter():
        if proc.name().lower() == proc_name:
            return proc.pid
    return 0

def getOrCreateGame() -> Game:
    global game
    try:
        if game == None:
            game = connectGame(findPid())
    except NameError:
        game = connectGame(findPid())
    return game
