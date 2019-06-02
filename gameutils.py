from memutils import getMemOps


def explainBuilding(buldingA):
    mem = getMemOps()
    print("building: " + hex(buldingA))
    print("buldingA + 0x1CC: " + hex(mem.readInteger(buldingA + 0x1CC)))
    print("buldingA + 0x1CC, 8: " + hex(mem.readInteger(buldingA + 0x1CC, 8)))
    print("queueItemA: " + hex(mem.readInteger(buldingA + 0x1CC, 8, 0)))
    print("timeCreating: " + str(mem.readFloat(buldingA + 0x1CC, 8, 0, 0x44)))
    print("unitType: " + str(mem.readInt16(buldingA + 0x1CC, 8, 0, 0x40)))