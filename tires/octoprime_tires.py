from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, wear_level):
        self.wear_level = wear_level
        
    def needs_service(self):
        return sum(self.wear_level) >= 3