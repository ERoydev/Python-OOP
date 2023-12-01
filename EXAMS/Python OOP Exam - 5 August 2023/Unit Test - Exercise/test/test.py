from project.second_hand_car import SecondHandCar
import unittest


class SimpleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.second_hand = SecondHandCar("Audi", "Sedan", 200, 1000)
        self.other_hand = SecondHandCar('BMW', "Sedan", 201, 1500)

    def test_initialization(self):
        self.assertEqual("Audi", self.second_hand.model)
        self.assertEqual("Sedan", self.second_hand.car_type)
        self.assertEqual(200, self.second_hand.mileage)
        self.assertEqual(1000, self.second_hand.price)
        self.assertEqual([], self.second_hand.repairs)

    def test_price_property(self):
        result = self.second_hand.price
        self.assertEqual(1000, result)

    def test_price_setter_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.second_hand.price = 0.9
        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.second_hand.price = -2
        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.second_hand.price = 1
        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))

        self.second_hand.price = 1.1
        self.assertEqual(1.1, self.second_hand.price)

    def test_price_setter(self):
        for value in range(2, 10, 1):
            self.second_hand.price = value
            self.assertEqual(value, self.second_hand.price)

    def test_mileage_property(self):
        result = self.second_hand.mileage
        self.assertEqual(200, result)

    def test_mileage_setter_exception(self):
        for value in range(100, -20, -10):
            with self.assertRaises(ValueError) as ex:
                self.second_hand.mileage = value

            self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ex.exception))

    def test_mileage_setter(self):
        for value in range(101, 300, 20):
            self.second_hand.mileage = value
            self.assertEqual(value, self.second_hand.mileage)

    def test_set_promotional_price_if_new_price_is_bigger_than_current_price_exception(self):
        for value in range(1000, 1300, 20):
            with self.assertRaises(ValueError) as ex:
                self.second_hand.set_promotional_price(value)

            self.assertEqual('You are supposed to decrease the price!', str(ex.exception))

    def test_set_promotional_price_if_new_price_is_less_than_current(self):
        self.assertEqual(1000, self.second_hand.price)

        for value in range(999, 800, -50):
            result = self.second_hand.set_promotional_price(value)
            self.assertEqual(value, self.second_hand.price)

            self.assertEqual('The promotional price has been successfully set.', result)

    def test_need_repair_if_its_impossible(self):
        for i in range(501, 800, 50):
            result = self.second_hand.need_repair(501, 'Repair Wheel')

            self.assertEqual('Repair is impossible!', result)

    def test_need_repair_if_possible(self):
        self.assertEqual([], self.second_hand.repairs)
        result = self.second_hand.need_repair(400, 'Wheels')
        self.assertEqual(f'Price has been increased due to repair charges.', result)
        self.assertEqual(1400, self.second_hand.price)
        self.assertEqual(['Wheels'], self.second_hand.repairs)

        result = self.second_hand.need_repair(200, 'Mirror')
        self.assertEqual(f'Price has been increased due to repair charges.', result)
        self.assertEqual(1600, self.second_hand.price)
        self.assertEqual(['Wheels', 'Mirror'], self.second_hand.repairs)

    def test_greater_than_dunder_method_if_cars_cant_be_compared(self):
        self.other_hand.car_type = "Combi"
        result = self.second_hand > self.other_hand
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)
        result = self.other_hand > self.second_hand
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_greater_than_dunder_method_if_it_works_correctly(self):
        result = self.second_hand > self.other_hand
        self.assertFalse(result)
        result = self.other_hand > self.second_hand
        self.assertTrue(result)

        self.second_hand.price = 1501
        result = self.second_hand > self.other_hand
        self.assertTrue(result)
        result = self.other_hand > self.second_hand
        self.assertFalse(result)

    def test_str_method(self):
        expected_result = f"""Model Audi | Type Sedan | Milage 200km
Current price: 1000.00 | Number of Repairs: 0"""
        result = str(self.second_hand)

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()