from __future__ import annotations
from Engine.Interfaces import EventListener
from typing import List, Union

_timers:List[TimerDefinition] = []

def GetTimer(timerID:int):
    return _timers[timerID]


class TimerDefinition:

    def __init__(self):
        _timers.append(self)
        self.uid = len(_timers) - 1

    def Listen(self, event:str, data:dict, timer:int)->int:
        pass


class Timer(EventListener):

    def __init__(self, uid:Union[int,TimerDefinition], timer:int):
        if isinstance(uid, TimerDefinition):
            uid = uid.uid
        self.uid = uid
        self.timer = timer

    def Listen(self, event:str, data:dict):
        self.timer = GetTimer(self.uid).Listen(event, data, self.timer)


class CountDownTimer(TimerDefinition):

    def __init__(self, eventUsed, terminatingEvents=()):
        TimerDefinition.__init__(self)
        if isinstance(terminatingEvents, str) or isinstance(terminatingEvents, int):
            terminatingEvents = (terminatingEvents,)
        self.event = eventUsed
        self.terminating_events = terminatingEvents

    def Listen(self, event:str, data:dict, timer:int):
        if event == self.event:
            return timer - 1
        if event in self.terminating_events:
            return 0
        return timer


class CountUpTimer(TimerDefinition):

    def __init__(self, eventUsed):
        TimerDefinition.__init__(self)
        self.event = eventUsed

    def Listen(self, event:str, data:dict, timer:int):
        if event == self.event:
            return timer + 1
        return timer
