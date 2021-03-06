from Engine.Save import SaveChunk, BinaryIO, SaveShort
from Engine.Unit import Unit
from EventEngine.Stage.TerrainMap import TerrainMap, _parse_coords
from queue import PriorityQueue
from Definitions.Tiles import WarpMovement

def In(x,y,max_x,max_y):
    return x in range(max_x) and y in range(max_y)

def EmptyArray2D(width, height, default):
    return [[default for _ in range(height)] for _ in range(width)]

def Set2Array2D(set, width, height):
    return [[(i,j) in set for j in range(height)] for i in range(width)]

def BorderMap(s):
    return set([(x,y) for x,y in s if (x-1, y) not in s or (x, y-1) not in s or (x+1,y) not in s or (x,y+1) not in s])

def FillMap(s, max_range, origin):
    n = 1000 # hard limit
    mx,my = max_range
    next = [origin]
    result = [i for i in s]
    for i in range(n):
        if len(next) == 0:
            break
        x, y = next[0]
        next = next[1:]
        if (x,y) in result:
            pass
        elif not In(x, y, mx, my):
            pass
        else:
            next.append((x-1,y))
            next.append((x,y-1))
            next.append((x+1,y))
            next.append((x,y+1))
            result.append((x,y))
    return result


class Stage(SaveChunk):

    def __init__(self):
        self.terrain = TerrainMap(0,0)
        self.units = []
        self.map_objects = []
        self.map_buffs = []

    def Read(self, stream:BinaryIO):
        self.terrain.Read(stream)
        n = SaveShort().Read(stream)
        self.units = self.map_objects = self.map_buffs = []
        for i in range(n):
            self.units.append(Unit().Read(stream))
        #TODO: map objects stuff

    def Write(self, stream:BinaryIO):
        self.terrain.Write(stream)
        SaveShort(len(self.units)).Write(stream)
        for i in self.units:
            i.Write(stream)

    def Width(self):
        return self.terrain.Width()

    def Height(self):
        return self.terrain.Height()

    def GetUnit(self, id_or_x, y=None):
        if y is None:
            for i in self.units:
                if i.id == id_or_x:
                    return i
        else:
            x, y = _parse_coords(id_or_x, y)
            for i in self.units:
                if i.coords == (x, y):
                    return i

    def GetMapObject(self, x, y=None):
        return None
        #x,y = _parse_coords(x, y)
        #return self.map_objects[x][y]

    def _MovementMap(self, coords, move_range, terrain_cost, allegiance_tuple):
        tiles = EmptyArray2D(self.Width(), self.Width(), 255)
        x, y = coords
        self._dijkstra(tiles, x, y, move_range, self._moveOntoFunc(terrain_cost, allegiance_tuple), self._moveAwayFunc())
        return tiles

    def MovementMap(self, coords, move_range, terrain_cost, allegiance_tuple):
        m = self._MovementMap(coords, move_range, terrain_cost, allegiance_tuple)
        result = set()
        result2 = set()
        for i,v in enumerate(m):
            for j,u in enumerate(v):
                if u <= move_range:
                    result.add((i,j))
                    if self.GetUnit(i, j) is None:
                        result2.add((i,j))
        return result, result2

    def WarpMap(self, coords, move_range, terrain_cost, allegiance_tuple):
        m = self._MovementMap(coords, move_range, WarpMovement, allegiance_tuple)
        result = set()
        result2 = set()
        for i,v in enumerate(m):
            for j,u in enumerate(v):
                if u <= move_range:
                    result.add((i,j))
                    if self.GetUnit(i, j) is None and terrain_cost[self.terrain.GetTerrain(i, j)] != 255:
                        result2.add((i,j))
        return result, result2

    def AttackMap(self, coords, target_range, allegiance_tuple):
        if isinstance(target_range, tuple):
            min_range, max_range = target_range
        else:
            min_range = 1
            max_range = target_range
        attack_map = []
        target_map = []
        x, y = coords
        for i in range(0, max_range + 1):
            for j in range(min_range - i if min_range > i else 0, max_range + 1 - i):
                for k,l in ((1,1),(1,-1),(-1,1),(-1,-1)):
                    if self.GetUnit(x + k * i, y + l * j) is not None:
                        if self.GetUnit(x + k * i, y + l * j).allegiance in allegiance_tuple:
                            target_map.append((x + k * i, y + l * j))
                    a, b = (x + k * i, y + l * j)
                    if not In(a, b, self.Width(), self.Height()):
                        continue
                    attack_map.append((a,b))
        return attack_map, target_map

    def AttackMapFromMovementMap(self, movement_map, target_range, allegiance_tuple):
        attack_map = set()
        target_map = set()
        for i in movement_map:
            a, t = self.AttackMap(i, target_range, allegiance_tuple)
            attack_map.update(a)
            target_map.update(t)
        return attack_map, target_map

    def MovementMapFromMovementMap(self, movement_map, move_range, terrain_cost, allegiance_tuple):
        result1 = set()
        result2 = set()
        for i in movement_map:
            a, t = self.MovementMap(i, move_range, terrain_cost, allegiance_tuple)
            result1.update(a)
            result2.update(t)
        return result1, result2

    def _dijkstra(self, tiles, x, y, max_range, move_onto_cost_func, move_away_cost_func):
        queue = PriorityQueue()
        queue.put((0, (x,y)))
        tiles[x][y] = 0
        visited = set()
        start = True
        arrows = ((-1,0), (1, 0), (0, -1), (0, 1))
        while not queue.empty():
            _, (x,y) = queue.get()
            if (x,y) in visited:
                continue
            visited.add((x,y))
            cost = tiles[x][y] + (move_away_cost_func(x, y) if not start else 0) # if start, no move away cost
            start = False
            for a, b in arrows:
                if not In(x+a, y+b, self.Width(), self.Height()):
                    continue
                if tiles[x+a][y+b] > cost:
                    tiles[x+a][y+b] = cost + move_onto_cost_func(x+a, y+b)
                    if tiles[x+a][y+b] < max_range:
                        queue.put((cost, (x+a, y+b)))

    def _moveOntoFunc(self, terrain_cost, allegiance_tuple):
        return lambda x, y: self._moveOntoCost(x,y,terrain_cost,allegiance_tuple)

    def _moveAwayFunc(self, guarded_tiles=()):
        return lambda x, y: self._moveAwayCost(x,y,guarded_tiles)

    def _moveOntoCost(self,x, y, terrain_cost, allegiance_tuple):
        if self.GetUnit(x,y) is not None and self.GetUnit(x,y).allegiance not in allegiance_tuple:
            return 255
        elif self.GetMapObject(x,y) is not None:
            return max(self.GetMapObject(x,y).TerrainCost(), terrain_cost[self.terrain.GetTerrain(x, y)])
        else:
            return terrain_cost[self.terrain.GetTerrain(x, y)]

    # only used if a unit has guard, which halts enemy movement
    # or called by traps
    # will not activate if movement starts on said tile
    def _moveAwayCost(self, x, y, guarded_tiles:list=()):
        return 255 if (x,y) in guarded_tiles else 0

    def GuardedTiles(self):
        return True
        # tiles = EmptyArray2D(self.Width(), self.Height(), False)
        # for x,y in self.map_objects:
        #     if self.map_objects[(x,y)].move_away_cost == MOVE_AWAY_COST:
        #         tiles[x][y] = True
        # for i in self.unit_by_id:
        #     if self.unit_by_id[i].HasBuff(GuardTileBuff):
        #         x,y = self.unit_by_id[i].GetCoords()
        #         arrows = ((0,-1), (0,1), (-1,0), (1,0))
        #         for a,b in arrows:
        #             if In(x+a, y+b, self.Width(), self.Height()):
        #                 tiles[x+a][y+b] = True
        # return tiles

MainStage = Stage()