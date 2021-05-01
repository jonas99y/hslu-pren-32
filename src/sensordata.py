from pathlib import Path
import time
from typing import Dict
import yaml
src_dir = Path(__file__).parent

class SensorData:
    def __init__(self, file:Path):
        self._file = file
        if not self._file.exists():
            open(self._file, 'w').close()

    def write(self, data: Dict):
        with open(self._file, "w") as f:
            yaml.safe_dump(data, f)

    def read(self) -> Dict:
        with open(self._file, "r") as f:
            data = yaml.safe_load(f)
            if not data:
                time.sleep(0.001)
                return self.read()
            else:
                return data

