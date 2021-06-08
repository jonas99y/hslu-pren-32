
from detection.pictogramcamera import PictogramCamera
from states.context import Context
from states.state import State


class ScanPictogramState(State):
    def __init__(self, nextState: State, cam: PictogramCamera):
        self._cam = cam
        super().__init__(nextState)

    def _start(self, context: Context) -> "State":
        result = self._cam.detect_pictogram()
        if result:
            context.pictogram = result
        # else:
            # rotate oder so!
