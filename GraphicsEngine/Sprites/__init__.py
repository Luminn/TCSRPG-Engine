
_sprites = []


def AddSprite(addr):
    _sprites.append(addr)
    return len(_sprites) - 1

def GetSprite(id):
    return _sprites[id]

_icons = {}

# used in text
def AddIcon(name, addr):
    index = AddSprite(addr)
    _icons[name] = index

def GetIcon(name):
    GetSprite(_icons[name])
