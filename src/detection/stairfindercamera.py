
class StairFinderCamera:
    def __init__(self):
        self.count = 0
    def is_stair_in_front(self)->bool:
        if self.count == 4:
            return True
        else:
            self.count+=1
            return False