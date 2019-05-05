from ctypes import *
from utils import *
from memutils import *

OpenProcess = windll.kernel32.OpenProcess
ReadProcessMemory = windll.kernel32.ReadProcessMemory
CloseHandle = windll.kernel32.CloseHandle

PROCESS_ALL_ACCESS = 0x1F0FFF

pid = 0x1A30   # I assume you have this from somewhere.
address = 0x019A21D8  # Likewise; for illustration I'll get the .exe header.
openProc(pid)
# buffer = c_int(5)
# bufferSize = 4
buffer = readByteArr(address, 8)
print(hex0(buffer.raw))
a = readInt(address)
print(a)
num = c_int(0)
bufferSize = 4
bytesRead = c_ulong(0)

if ReadProcessMemory(processHandle, address, byref(num), bufferSize, byref(bytesRead)):
    print("Success: " + str(num.value))
else:
    print("Failed. " + str(num.value))
print(bytesRead.value)
print(hex0(num.value))

CloseHandle(processHandle)

