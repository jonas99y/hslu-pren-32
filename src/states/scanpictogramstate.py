
from detection.pictogramcamera import PictogramCamera
from states.context import Context
from states.state import State
class ScanPictogramState(State):
    def __init__(self, nextState:State, cam:PictogramCamera):
        self._nextState = nextState
        self._cam = cam

    def cycle(self, context:Context) -> "State":
        result = self._cam.detect_pictogram()
        if result:
            context.pictogram = result
            return self._nextState
        # else:
            # rotate oder so!
        return self