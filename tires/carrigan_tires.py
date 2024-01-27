from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, wear_level):
        self.wear_level = wear_level
        
    def needs_service(self):
        return any(wear >= 0.9 for wear in self.wear_level)