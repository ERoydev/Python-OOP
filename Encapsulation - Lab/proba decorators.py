
class Car:
    def __init__(self, max_speed: int):
        self.max_speed = max_speed

    def drive(self):
        print(f'driving max speed {self.max_speed}')

    @property
    def max_speed(self):
        return self.__max_speed
    
    @max_speed.setter
    def max_speed(self, value):
        if value > 200:
            value = 200
        self.__max_speed = value

red_car = Car(233)
red_car.max_speed = 400
print(red_car.max_speed)



