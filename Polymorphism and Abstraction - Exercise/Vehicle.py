from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self,fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def drive(self, distance):
        fuel_to_spend = (self.fuel_consumption + 0.9) * distance
        if fuel_to_spend > self.fuel_quantity:
            return

        self.fuel_quantity -= fuel_to_spend

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def drive(self, distance):
        fuel_to_spend = (self.fuel_consumption + 1.6) * distance
        if fuel_to_spend > self.fuel_quantity:
            return

        self.fuel_quantity -= fuel_to_spend

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
