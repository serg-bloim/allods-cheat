from ctypes import *

OpenProcess = windll.kernel32.OpenProcess
ReadProcessMemory = windll.kernel32.ReadProcessMemory
CloseHandle = windll.kernel32.CloseHandle

PROCESS_ALL_ACCESS = 0x1F0FFF
def openProc(pid):
    global processHandle
    processHandle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)

def readInteger(addr):
    num = c_int(0)
    bufferSize = 4
    bytesRead = c_ulong(0)
    if ReadProcessMemory(processHandle, addr, byref(num), bufferSize, byref(bytesRead)):
        print("Success: " + str(num.value))
    else:
        print("Failed. " + str(num.value))
    return num.value


def readByteArr(addr, size):
    from utils import hex0
    global processHandle
    buffer = create_string_buffer(size)
    bytesRead = c_ulong(0)
    if ReadProcessMemory(processHandle, addr, buffer, c_int(size), byref(bytesRead)) and bytesRead.value == size:
        print("Success: " + hex0(buffer.raw))
    else:
        print("Failed. " + hex0(buffer.raw))
    return buffer


def readInt(addr):
    return cast(readByteArr(addr, 4), POINTER(c_int)).contents.value