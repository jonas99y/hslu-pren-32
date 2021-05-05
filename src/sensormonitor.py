from typing import Callable
from sensordata import SensorData
import time
from abc import ABC, abstractmethod

class Handle(ABC):
    @abstractmethod
    def deregister(self):
        pass

class MonitorHandle(Handle):
    def __init__(self, sensorMonitor:any):
        self._monitor = sensorMonitor

    def deregister(self):
        self._monitor._monitors.pop(self)

class SensorMonitor:
    def __init__(self, sensorData: SensorData):
        self._sensorData = sensorData
        self._monitors = {}
        self._lastData = {}
        
    def cycle(self):
        data = self._sensorData.read()
        for key in data:
            if key in self._lastData:
                if data[key] != self._lastData[key]:
                    self._alert_subs(key, data[key])
        self._lastData = data
        time.sleep(0.1)



    def _alert_subs(self, key:str, value:any):
        for subbedKey, callback in self._monitors.values():
            if subbedKey == key:
                callback(value)


    def monitor(self, key: str, callback: Callable[[any],None]) -> Handle:
        handle = MonitorHandle(self)
        self._monitors[handle] = (key, callback)
        data = self._sensorData.read()




