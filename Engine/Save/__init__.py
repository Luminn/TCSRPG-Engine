from typing import BinaryIO
import struct
import base64


def to_unsigned(num, pow):
    num &= (1 << pow) - 1
    if num < 0:
        num += 1 << pow
    return num

def signed_compare(n1, n2, pow):
    return to_unsigned(n1, pow) == to_unsigned(n2, pow)

# a chunk of save data
class SaveChunk:
    def Read(self, stream:BinaryIO):
        pass

    def Write(self, stream:BinaryIO):
        pass


class SaveInt(SaveChunk):

    def __init__(self, i:int=0):
        self.data = to_unsigned(i, 32)

    def Read(self, stream:BinaryIO) -> int:
        i = stream.read(4)
        (self.data,) = struct.unpack(">I", i)
        return self.data

    def Write(self, stream:BinaryIO):
        i = struct.pack(">I", self.data)
        stream.write(i)

    def __int__(self):
        return self.data

class SaveShort(SaveChunk):

    def __init__(self, i:int=0):
        self.data = to_unsigned(i, 16)

    def Read(self, stream:BinaryIO) -> int:
        i = stream.read(2)
        (self.data,) = struct.unpack(">H", i)
        return self.data

    def Write(self, stream:BinaryIO):
        i = struct.pack(">H", self.data)
        stream.write(i)

    def __int__(self):
        return self.data

class SaveByte(SaveChunk):

    def __init__(self, i:int=0):
        self.data = to_unsigned(i, 8)

    def Read(self, stream:BinaryIO) -> int:
        i = stream.read(1)
        (self.data,) = struct.unpack(">B", i)
        return self.data

    def Write(self, stream:BinaryIO):
        i = struct.pack(">B", self.data)
        stream.write(i)

    def __int__(self):
        return self.data

class SaveBool(SaveChunk):

    def __init__(self, i:bool=False):
        self.data = i

    def Read(self, stream:BinaryIO) -> int:
        i = stream.read(1)
        (self.data,) = bool(struct.unpack(">B", i))
        return self.data

    def Write(self, stream:BinaryIO):
        i = struct.pack(">B", int(self.data))
        stream.write(i)

    def __bool__(self):
        return self.data

class SaveString(SaveChunk):

    def __init__(self, s:str=""):
        self.data = s

    def Read(self, stream:BinaryIO) -> str:
        i = SaveShort().Read(stream)
        s = base64.b64decode(stream.read(i)).decode("utf-8")
        self.data = s
        return s

    def Write(self, stream:BinaryIO):
        s = base64.b64encode(self.data.encode("utf-8"))
        stream.write(struct.pack(">H", len(s)))
        stream.write(s)

    def __str__(self):
        return self.data