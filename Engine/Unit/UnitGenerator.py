from Engine.Unit import Unit
import Engine.Buff.Stats as Stats

def GenerateUnit(allegiance, ):
    u = Unit()
    u.id = Unit.GetNextID()
    u._storeUnit()
    u.SetStat(Stats.MaxHP, 20)
    u.SetStat(Stats.Strength, 4)
    u.SetStat(Stats.Magic, 1)
    u.SetStat(Stats.Defense, 9)
    u.SetStat(Stats.Resistance, 4)
    u.SetStat(Stats.Speed, 13)
    u.SetStat(Stats.Draw, 4)
    u.SetStat(Stats.Movement, 5)
    return u

