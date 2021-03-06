from Engine.Save import SaveChunk, SaveShort

# just put a bunch of globals here, save those in a file with a class


Resolution_X, Resolution_Y = 800, 600
FullScreen = 0
FastMode = 0
RightClickMovementCards = 0

class SaveData(SaveChunk):

    def Write(self, stream):
        SaveShort(Resolution_X).Write(stream)
        SaveShort(Resolution_Y).Write(stream)
        SaveShort(FullScreen).Write(stream)
        SaveShort(FastMode).Write(stream)
        SaveShort(RightClickMovementCards).Write(stream)

    def Read(self, stream):
        global Resolution_X, Resolution_Y, FullScreen, FastMode, RightClickMovementCards
        Resolution_X = SaveShort().Read(stream)
        Resolution_Y = SaveShort().Read(stream)
        FullScreen = SaveShort().Read(stream)
        FastMode = SaveShort().Read(stream)
        RightClickMovementCards = SaveShort().Read(stream)


