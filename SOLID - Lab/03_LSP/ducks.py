from abc import abstractmethod, ABC


class Duck(ABC):

    @staticmethod
    def quack():
        pass


class RubberDuck(Duck):
    @staticmethod
    def quack():
        return "Squeek"


class Flyable:
    @staticmethod
    def fly():
        pass


class Walkable:
    @staticmethod
    def walk():
        pass


class RobotDuck(Duck, Walkable, Flyable):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    @staticmethod
    def fly():
        return "Robotic flying"

robot_duck = RobotDuck()
print(robot_duck.fly())