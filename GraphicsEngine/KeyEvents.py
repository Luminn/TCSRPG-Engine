
from GraphicsEngine.TileMap.MapCursor import CursorCoords
from EventEngine.Stage import MainStage
import EventEngine.MainEngine as ME
# called by clicking x and/or click lmb on unit

def HandleClick():
    x, y = CursorCoords()
    u = MainStage.GetUnit(x, y)
    if u is None:
        ME.OnSelectTile((x,y))
    else:
        ME.OnSelectUnit(u)

def HandleSecondaryClick():
    x, y = CursorCoords()
    u = MainStage.GetUnit(x, y)
    if u is not None:
        ME.OnSecondarySelectUnit(u)