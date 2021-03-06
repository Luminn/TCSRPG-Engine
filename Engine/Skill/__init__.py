
from Engine.Buff.BuffList import BuffList

_skill_list = []

def GetSkill(i):
    return _skill_list[i]


class Skill(BuffList):

    def __init__(self, name, description):
        _skill_list.append(self)
        self.id = len(_skill_list) - 1
        self.name = name
        self.description = description