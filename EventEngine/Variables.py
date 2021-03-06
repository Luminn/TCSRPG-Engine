from Engine.Unit import DummyUnit

TurnUserLockedIn = False
CurrentUnit = DummyUnit
RangePromptOn = False
AdvancedRangePromptOn = False
PromptUnit = DummyUnit
PromptType = 0
SelectedCardOrSkill = 0 # 0+ are cards, - are skills

# refund when save
RefundQueue = [] # cleared after attack prompt selected, turn end, etc, stores (previous position (x,y), vigor_cost)
PromptNo = 0
PromptMove = 1
PromptAttack = 2
PromptDisplay = 2
PromptTargets = []