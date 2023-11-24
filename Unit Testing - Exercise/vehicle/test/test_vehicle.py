import unittest
from vehicle.project.vehicle import Vehicle


class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.vehicle = Vehicle(100, 120)

    def test_default_consumption_class_attribute_is_correct(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_if_initialized_correctly(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(120, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_if_fuel_is_not_enough_raises_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual(str(ex.exception), "Not enough fuel")
        self.assertEqual(0, self.vehicle.fuel)

    def test_drive_if_fuel_is_enough_decreasing_fuel_attribute(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.vehicle.drive(70)
        self.assertEqual(12.5, self.vehicle.fuel)
        self.vehicle.fuel = 100
        self.vehicle.drive(80)
        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel_too_much_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(15)

        self.assertEqual("Too much fuel", str(ex.exception))
        self.vehicle.drive(50)

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(65)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_if_fuel_is_increased_with_provided_amount(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(100)
        self.assertEqual(100, self.vehicle.fuel)
        self.vehicle.drive(50)
        self.vehicle.refuel(50)
        self.assertEqual(87.5, self.vehicle.fuel)

    def test_str_method_representation(self):
        expected_result = f"The vehicle has 120 " \
               f"horse power with 100 fuel left and 1.25 fuel consumption"

        result = str(self.vehicle)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()