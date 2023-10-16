from multilevel.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self,name, model):
        self.name = name
        self.model = model

    def drive(self):
        return "driving..."
