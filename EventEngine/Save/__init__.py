
from EventEngine.Save import SaveFileHeader, Settings, Roster
from EventEngine.Stage import MainStage

def Save(save_file_id):
    with open("Save/{}.ccsf.tmp".format(save_file_id)) as file:
        SaveFileHeader.SaveFileHeader.Write(file)
        Settings.LocalSettings.Write(file)
        Roster.MainRoster.Write(file)
        MainStage.Write(file)


