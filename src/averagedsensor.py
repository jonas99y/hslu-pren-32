
from Bluetin_Echo.Bluetin_Echo import Echo


class AveragedSensor:
    def __init__(self, echo: Echo):
        self._echo = echo
        self._lastValue = 5
        self._buffer = [1,1,1]

    def read(self,)-> float:
        v0 = self._echo.read()
        if v0 >0 and v0< 1000:
            self._lastValue = v0
            return v0
        else:
            return self._lastValue
        self._buffer.append(v0)
        total = 0
        amountOfValues = 0
        for v in self._buffer:
            if v >0 and v< 1000:
                total +=v
                amountOfValues +=1
        if amountOfValues == 0:
            return 0
        avg = total / amountOfValues
        self._buffer = self._buffer[1:len(self._buffer)]
        return avg
