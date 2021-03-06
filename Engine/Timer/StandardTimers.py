from Engine.Timer import TimerDefinition, CountDownTimer
import Definitions.Eventing as Events


class _NoTimer(TimerDefinition):
    def Listen(self, event:str, data:dict, timer):
        return 1

NoTimer = _NoTimer().uid
PersonalTurnTimer = CountDownTimer(Events.StartTurnUnit, Events.EndBattle).uid
PersonalEndTurnTimer = CountDownTimer(Events.EndTurnUnit, Events.EndBattle).uid
GlobalTurnTimer = CountDownTimer(Events.EndTurnGlobal, Events.EndBattle).uid
BattleTimer = CountDownTimer(Events.EndBattle).uid

