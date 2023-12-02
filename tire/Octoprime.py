from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, arr):
        self.arr = arr

    def needs_service(self):
        if sum(self.arr) >=3:
            return True