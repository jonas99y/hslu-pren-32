from pathlib import Path
import time
from typing import Dict
import yaml
src_dir = Path(__file__).parent

file = src_dir / 'sensor'



def write(data: Dict):
    with open(file, "w") as f:
        yaml.dump(data, f)

def read() -> Dict:
    with open(file, "r") as f:
        data = yaml.load(f)
        if not data:
            time.sleep(0.001)
            return read()
        else:
            return data
