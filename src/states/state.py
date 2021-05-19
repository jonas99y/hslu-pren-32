
from states.context import Context


class State:
    def cycle(self, context:Context) -> "State":
        return self
