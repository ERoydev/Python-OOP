class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)


from unittest import TestCase, main


class CarTest(TestCase):

    def test_initialization_check(self):
        vehicle = Car("China", "Audi", 10, 15)

        self.assertEqual("China", vehicle.make)
        self.assertEqual("Audi", vehicle.model)
        self.assertEqual(10, vehicle.fuel_consumption)
        self.assertEqual(15, vehicle.fuel_capacity)
        self.assertEqual(0, vehicle.fuel_amount)

    def test_make_property_with_empty_input(self):
        with self.assertRaises(Exception) as ex:
            vehicle = Car("", "Audi", 10, 15)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_property_to_return_value(self):
        vehicle = Car("China", "Audi", 10, 15)

        result = vehicle.make

        self.assertEqual("China", result)

    def test_make_property_with_none_input(self):
        with self.assertRaises(Exception) as ex:
            vehicle = Car(None, "Audi", 10, 15)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_property_with_empty_input(self):
        with self.assertRaises(Exception) as ex:
            vehicle = Car("China", "", 10, 15)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_with_none_value(self):
        with self.assertRaises(Exception) as ex:
            vehicle = Car("China", None, 10, 15)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_property_to_return_value(self):
        vehicle = Car("China", "Audi", 10, 15)

        result = vehicle.model

        self.assertEqual("Audi", result)

    def test_fuel_consumption_with_zero_input(self):
        with self.assertRaises(Exception) as ex:
            vehicle = Car("China", "Audi", 0, 15)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_with_negative_input(self):
        with self.assertRaises(Exception) as ex:
            vehicle = Car("China", "Audi", -1, 15)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_with_correct_input(self):
        vehicle = Car("China", "Audi", 10, 15)

        result = vehicle.fuel_consumption

        self.assertEqual(10, result)

    def test_fuel_capacity_with_zero_input(self):
        with self.assertRaises(Exception) as ex:
            vehicle = Car("China", "Audi", 15, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_negative_input(self):
        with self.assertRaises(Exception) as ex:
            vehicle = Car("China", "Audi", 15, -12)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_correct_input(self):
        vehicle = Car("China", "Audi", 10, 15)

        result = vehicle.fuel_consumption

        self.assertEqual(10, result)

    def test_fuel_amount_with_negative_input(self):
        vehicle = Car("China", "Audi", 10, 15)

        with self.assertRaises(Exception) as ex:
            vehicle.fuel_amount = -2

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount_with_correct_data(self):
        vehicle = Car("China", "Audi", 10, 15)

        vehicle.refuel(13)

        self.assertEqual(13, vehicle.fuel_amount)

    def test_refuel_with_zero_input(self):
        vehicle = Car("China", "Audi", 10, 15)

        with self.assertRaises(Exception) as ex:
            vehicle.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_negative_input(self):
        vehicle = Car("China", "Audi", 10, 15)

        with self.assertRaises(Exception) as ex:
            vehicle.refuel(-123)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_increment_data_correctly(self):
        vehicle = Car("China", "Audi", 10, 15)

        self.assertEqual(0, vehicle.fuel_amount)

        vehicle.refuel(5)
        self.assertEqual(5, vehicle.fuel_amount)
        vehicle.refuel(7)
        self.assertEqual(12, vehicle.fuel_amount)

    def test_refuel_with_data_bigger_than_capacity(self):
        vehicle = Car("China", "Audi", 10, 15)

        vehicle.refuel(20)

        self.assertEqual(15, vehicle.fuel_amount)

    def test_drive_with_bigger_distance(self):
        vehicle = Car("China", "Audi", 10, 15)

        with self.assertRaises(Exception) as ex:
            vehicle.drive(245)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_enough_fuel_to_drive(self):
        vehicle = Car("China", "Audi", 10, 15)

        vehicle.fuel_amount = vehicle.fuel_capacity

        vehicle.drive(100)

        self.assertEqual(5, vehicle.fuel_amount)


if __name__ == "__main__":
    main()