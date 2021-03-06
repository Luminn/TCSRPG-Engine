
from Engine.Save import SaveChunk, BinaryIO, SaveShort, SaveByte

def _parse_coords(x_or_coords, y=None):
    if y is None:
        return x_or_coords
    return x_or_coords, y

class TerrainMap(SaveChunk):

    def __init__(self, width=0, height=0):
        self.data = [[0 for _ in range(width)] for _ in range(height)]

    def Width(self):
        if len(self.data) == 0:
            return 0
        return len(self.data[0])

    def Height(self):
        return len(self.data)


    def GetTerrain(self, x_or_coords, y=None):
        x, y = _parse_coords(x_or_coords, y)
        return self.data[x][y]

    def Read(self, stream:BinaryIO):
        w, h = SaveShort().Read(stream), SaveShort().Read(stream)
        self.data = [[SaveByte().Read(stream) for _ in range(w)] for _ in range(h)]

    def Write(self, stream:BinaryIO):
        SaveShort(self.Width()).Write(stream)
        SaveShort(self.Height()).Write(stream)
        for i in self.data:
            for j in i:
                SaveByte(j).Write(stream)




