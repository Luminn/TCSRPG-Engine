from Engine.Save import SaveChunk
from typing import BinaryIO
from Engine.Save import SaveShort, SaveInt
import struct


class SaveShortArray(SaveChunk, list):
    def __init__(self, arr:list=()):
        list.__init__(self, arr)

    def Read(self, stream:BinaryIO) -> list:
        self.clear()
        i = SaveShort().Read(stream)
        self.extend([struct.unpack(">H", stream.read(2))[0] for _ in range(i)])
        return self

    def Write(self, stream:BinaryIO):
        SaveShort(len(self)).Write(stream)
        for i in self:
            SaveShort(i).Write(stream)



class SaveIntArray(SaveChunk, list):
    def __init__(self, arr:list=()):
        list.__init__(self, arr)

    def Read(self, stream:BinaryIO) -> list:
        self.clear()
        i = SaveShort().Read(stream)
        self.extend([struct.unpack(">I", stream.read(4))[0] for _ in range(i)])
        return self

    def Write(self, stream:BinaryIO):
        SaveShort(len(self)).Write(stream)
        for i in self:
            SaveInt(i).Write(stream)

