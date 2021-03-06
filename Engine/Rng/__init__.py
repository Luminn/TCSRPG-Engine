from random import Random
from Definitions.Rng import *
from Engine.Save.Arrays import SaveIntArray

RNG_MULTIPLIER = 1103515245
RNG_INCREMENT = 12820163
SEED_MAX = 4294967296


# implement this with a buff or something
class RandomElement:
    def __init__(self, seed=0):
        self.SetSeed(seed % SEED_MAX)

    def GetSeed(self)->int:
        pass

    def SetSeed(self, seed:int):
        pass

    def Next(self)->int:
        self.SetSeed(RandomNumberGenerator.NextSeed(self.GetSeed()))
        return self.GetSeed()

    def Advance(self, num:int):
        [self.Next() for _ in range(num)]

    def RandInt(self, min_or_max, max=-1):
        if max == -1:
            return self.Next() * min_or_max // SEED_MAX
        else:
            return self.Next() * (max - min_or_max) // SEED_MAX + min_or_max


class RandomNumberGenerator(SaveIntArray):

    @staticmethod
    def NextSeed(seed:int):
        return (seed * RNG_MULTIPLIER + RNG_INCREMENT) % SEED_MAX

    def RandInt(self, seed, min_or_max, max=-1):
        if max == -1:
            return self.Next(seed) * min_or_max // SEED_MAX
        else:
            return self.Next(seed) * (max - min_or_max) // SEED_MAX + min_or_max

    def __init__(self,saved_seeds:int, unsaved_seeds:int):
        SaveIntArray.__init__(self)
        rand = Random()
        self.extend([rand.randint(0, SEED_MAX) for _ in range(saved_seeds)])
        self.unsaved_seeds = [rand.randint(0, SEED_MAX) for _ in range(unsaved_seeds)]

    def Next(self, seed:int):
        length = len(self)
        if seed < length:
            self[seed] = RandomNumberGenerator.NextSeed(self[seed])
            return self[seed]
        else:
            self.unsaved_seeds[seed - length] = RandomNumberGenerator.NextSeed(self.unsaved_seeds[seed - length])
            return self.unsaved_seeds[seed - length]


MainRNG = RandomNumberGenerator(SavedRNGCount, UnsavedRNGCount)