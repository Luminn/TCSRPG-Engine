
from EventEngine.Stage import MainStage


def GetUnitsSprites():
    for i in MainStage.units:
        if not i.GetStat("is_invisible") and i.map_unit is not None:
            yield i.map_unit
