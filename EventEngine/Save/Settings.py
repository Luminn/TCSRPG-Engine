
from Engine.Save import SaveChunk

class MainSettings(SaveChunk):
    pass


class SaveFileSettings(SaveChunk):
    pass


GlobalSettings = MainSettings()
LocalSettings = SaveFileSettings()