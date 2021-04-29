from pathlib import Path
import time
src_dir = Path(__file__).parent

file = src_dir / 'sensor'


class SensorData():
    def __init__(self, value:int) -> None:
        self.value = value


def write(data: SensorData):
    with open(file, "w") as f:
            f.write(str(data.value))

def read() -> SensorData:
    with open(file, "r") as f:
        text = f.read()
        if len(text) == 0:
            time.sleep(0.001)
            return read()
        else:
            return text
