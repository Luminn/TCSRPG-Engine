

ID = "id"
SEED = "seed"
NAME = "name"
ALLEGIANCE = "allegiance"

MALE = 0
FEMALE = 1

X = "x"
Y = "y"
VISIBLE = "visible"
ALIVE = "alive"

CLASS = "classification"
SKILLS = "skills"
CLASS_SKILLS = "class_skills"
ITEM1 = "item1"
ITEM2 = "item2"
ITEM3 = "item3"
INVENTORY = "inventory"
MAX_VIGOR = "max_vigor"
VIGOR = "current_vigor"

MAX_HP = "max_hp"
HP = "current_hp"
STRENGTH = "strength"
MAGIC = "magic"
DEFENSE = "defense"
RESISTANCE = "resistance"
SPEED = "speed"
DRAW = "draw"
MOVEMENT = "movement"



HP_GROWTH = "max_hp_growth"
STRENGTH_GROWTH = "strength_growth"
MAGIC_GROWTH = "magic_growth"
DEFENSE_GROWTH = "defense_growth"
RESISTANCE_GROWTH = "resistance_growth"
SPEED_GROWTH = "speed_growth"
DRAW_GROWTH = "draw_growth"
MOVEMENT_GROWTH = "movement_growth"

DECK = "deck"
TEMP_DECK = "temp_deck"
HAND = "hand"
DRAW_PILE = "draw_pile"
DISCARD_PILE = "discard_pile"

# stats that has a growth
GrowthStats = (MAX_HP, STRENGTH, MAGIC, DEFENSE, RESISTANCE, SPEED, DRAW, MOVEMENT)

# halves growth after a growth
DiminishingGrowth = (DRAW, MOVEMENT)

# stats that goes through the stat calc loop, notably no hp & current hp
CalcLoopStats = (STRENGTH, MAGIC, DEFENSE, RESISTANCE, SPEED, MOVEMENT, DRAW,
                 HP_GROWTH, STRENGTH_GROWTH, MAGIC_GROWTH, DEFENSE_GROWTH, RESISTANCE_GROWTH, SPEED_GROWTH,
                 MOVEMENT_GROWTH, DRAW_GROWTH)

GrowthSuffix = "_growth"
MaxPrefix = "max_"
CurrPrefix = "current_"

TEMP_BUFFS = "temp_buffs"
