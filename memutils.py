from _ctypes import _SimpleCData
from ctypes import *

OpenProcess = windll.kernel32.OpenProcess
ReadProcessMemory = windll.kernel32.ReadProcessMemory
CloseHandle = windll.kernel32.CloseHandle

PROCESS_ALL_ACCESS = 0x1F0FFF


def openProc(pid):
    global currentHandle
    currentHandle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    return currentHandle


class MemUtils:
    def __init__(self, handle):
        self.handle = handle
        self.debugPtrs = True

    def readInteger(self, addr, *offsets):
        return self.readByPointer(c_int, addr, *offsets)

    def readByteArr(self, addr, size):
        from utils import hex0
        global processHandle
        buffer = create_string_buffer(size)
        bytesRead = c_ulong(0)
        if ReadProcessMemory(self.handle, addr, buffer, c_int(size), byref(bytesRead)) and bytesRead.value == size:
            print("Success: " + hex0(buffer.raw))
        else:
            print("Failed. " + hex0(buffer.raw))
        return buffer

    def readInt(self, addr):
        return cast(self.readByteArr(addr, 4), POINTER(c_int)).contents.value

    def pointers(self, addr, offset=-1, *args):
        if offset == -1:
            return addr
        elif len(args) == 0:
            resolved = self.readInteger(addr)
            if self.debugPtrs:
                print('[{0:X}:{1:X}]+{2:X}->'.format(addr, resolved, offset))
            return resolved + offset
        else:
            resolved = self.readInteger(addr)
            if self.debugPtrs:
                print('[{0:X}:{1:X}]+{2:X}:{3:X}->'.format(addr, resolved, offset, resolved + offset))
            return self.pointers(resolved + offset, *args)

    def readByPointer(self, type, addr, *offsets):
        contents = cast(self.readByteArr(self.pointers(addr, *offsets), sizeof(type)), POINTER(type)).contents
        if isinstance(contents, _SimpleCData):
            return contents.value
        return contents

    def readInt16(self, addr, *offsets):
        return self.readByPointer(c_int16, addr, *offsets)

    def readFloat(self, addr, *offsets):
        return self.readByPointer(c_float, addr, *offsets)


def getMemOps() -> MemUtils:
    global gmemOps
    global currentHandle
    try:
        gmemOps
    except NameError:
        gmemOps = MemUtils(currentHandle)
    return gmemOps
