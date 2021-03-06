
Player = 0
Enemy = 1
Neutral = 2
Ally = 3
Enemy2 = 4

PlayerMovement = (0, 2, 3)
EnemyMovement = (1, 2)
EnemyMovement2 = (4, 2)

PlayerTarget = (1, 4)
Enemy1Target = (0, 3, 4)
Enemy2Target = (0, 3, 1)

def MoveThrough(allegiance):
    if allegiance == Player or allegiance == Ally:
        return PlayerMovement
    elif allegiance == Enemy:
        return EnemyMovement
    elif allegiance == Enemy2:
        return EnemyMovement2
    else:
        return allegiance,