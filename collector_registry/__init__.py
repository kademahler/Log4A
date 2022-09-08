from dataclasses import dataclass
from datetime import datetime
from typing import Callable, Any, List

@dataclass
class TimeRange:
    BEGIN_TIME: datetime = None
    END_TIME: datetime = None

collectors_time_range = TimeRange()

@dataclass
class Collector:
    function: Callable[..., Any]
    is_timed: bool

    def __call__ (self) -> Any:
        if self.is_timed:
            return self.function(collectors_time_range.BEGIN_TIME, collectors_time_range.END_TIME)
        return self.function()

    @property
    def name(self) -> str:
        return self.function.__name__

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name

ALL_COLLECTORS: List[Collector]
ALL_COLLECTORS = []

def set_begin_time(begin_time: datetime):
    collectors_time_range.BEGIN_TIME = begin_time
def set_end_time(end_time: datetime):
    collectors_time_range.END_TIME = end_time

def _register_collector(collector_function: Callable[..., Any], is_timed: bool) -> None:
    ALL_COLLECTORS.append(Collector(collector_function, is_timed))

def general_collector():
    def decorator(collector_function) -> None:
        _register_collector(collector_function, False)
    return decorator
        

def timed_collector(file) -> None:
    def decorator(collector_function) -> None:
        _register_collector(collector_function, True)
    return decorator
    


