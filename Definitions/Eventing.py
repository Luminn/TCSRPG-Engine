
EventNone = "Event None"
StartDungeon = "Start Dungeon"
EndDungeon = "End Dungeon"
StartBattle = "Start Battle"
EndBattle = "End Battle"
StartTurnGlobal = "Start Turn Global"
EndTurnGlobal = "End Turn Global"
StartTurnUnit = "Start Turn Unit"
EndTurnUnit = "End Turn Unit"
StartEvent = "Start Event"
EndEvent = "End Event"


# before stats calc loop
BeforeAttack = 10
# after stats calc loop, for pre battle stuff
BeforeAttackCalcLoop = 11
# before death calculation, major battle stuff
OnAttackCalcLoop = 12
# right before death calculation, raise hp above 0 to not kill unit
DeathCalcLoop = 13
# after death calculation, don't kill/revive people here
AfterAttackCalcLoop = 14
# events after battle loop
EndAttack = 15

# these will not be called if battle loop is called for simplicity
BeforeCardPlay = 16
# called after card is played
AfterCardPlay = 17

# before event code is executed
BeforeEventChoice = 18
# after event code is executed
AfterEventChoice = 19