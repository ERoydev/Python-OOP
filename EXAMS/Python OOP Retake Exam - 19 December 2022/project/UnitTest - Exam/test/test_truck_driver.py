from project.truck_driver import TruckDriver
import unittest


class SimpleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver('Emil', 5)

    def test_initialization(self):
        self.assertEqual('Emil', self.driver.name)
        self.assertEqual(5, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_property(self):
        result = self.driver.earned_money
        self.assertEqual(0, result)

    def test_if_earned_money_less_than_zero_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.driver.earned_money = -1

        self.assertEqual(f"Emil went bankrupt.", str(ex.exception))
        self.driver.earned_money = 0
        self.assertEqual(0, self.driver.earned_money)

    def test_add_cargo_offer_if_cargo_location_already_added_exception(self):
        self.driver.available_cargos['city'] = 15

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer('city', 15)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_if_location_dont_exist(self):
        self.assertEqual({}, self.driver.available_cargos)
        result = self.driver.add_cargo_offer('city', 15)
        self.assertEqual(f"Cargo for 15 to city was added as an offer.", result)
        self.assertEqual({'city': 15}, self.driver.available_cargos)

    def test_drive_best_cargo_if_offers_not_available_exception(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_if_offers_are_available(self):
        self.driver.available_cargos = {'city': 15, 'town': 20, 'country': 16}
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

        self.driver.drive_best_cargo_offer()
        self.assertEqual(100, self.driver.earned_money)
        self.assertEqual(20, self.driver.miles)

        self.driver.available_cargos = {'city': 15, 'town': 16, 'country': 17}
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(185, self.driver.earned_money)
        self.assertEqual(37, self.driver.miles)

        self.assertEqual(f"Emil is driving 17 to country.", result)

    def test_eat(self):
        self.driver.earned_money = 200
        self.driver.eat(250)
        self.assertEqual(180, self.driver.earned_money)
        self.driver.eat(500)
        self.assertEqual(160, self.driver.earned_money)
        self.driver.eat(200)
        self.assertEqual(160, self.driver.earned_money)
        self.driver.eat(750)
        self.assertEqual(140, self.driver.earned_money)

    def test_sleep(self):
        self.driver.earned_money = 1000
        for miles in range(1000, 10001, 1000):
            expected_result = self.driver.earned_money - 45
            self.driver.sleep(miles)
            self.assertEqual(expected_result, self.driver.earned_money)

        self.driver.earned_money = 100
        self.driver.sleep(543)
        self.assertEqual(100, self.driver.earned_money)

    def test_pump_gas(self):
        self.driver.earned_money = 100000
        for miles in range(1500, 10001, 1500):
            expected_result = self.driver.earned_money - 500
            self.driver.pump_gas(miles)
            self.assertEqual(expected_result, self.driver.earned_money)

        self.driver.earned_money = 100
        self.driver.pump_gas(1543)
        self.assertEqual(100, self.driver.earned_money)

    def test_repair_truck(self):
        self.driver.earned_money = 100000

        for miles in range(10000, 50001, 10000):
            expected_result = self.driver.earned_money - 7500
            self.driver.repair_truck(miles)
            self.assertEqual(expected_result, self.driver.earned_money)

    def test_repr_method(self):
        result = repr(self.driver)
        self.assertEqual(f"Emil has 0 miles behind his back.", result)

    def test_check_for_activities(self):
        self.driver.earned_money = 1000
        self.driver.available_cargos = {'city': 15, 'town': 20, 'country': 250}
        self.driver.drive_best_cargo_offer()
        self.assertEqual(2230, self.driver.earned_money)

        self.driver.available_cargos = {'city': 15, 'town': 20, 'country': 1000}
        self.driver.drive_best_cargo_offer()
        self.assertEqual(7105, self.driver.earned_money)

        self.driver.available_cargos = {'city': 15, 'town': 20, 'country': 1500}
        self.driver.drive_best_cargo_offer()
        self.assertEqual(13940, self.driver.earned_money)

        self.driver.available_cargos = {'city': 15, 'town': 20, 'country': 10000}
        self.driver.drive_best_cargo_offer()
        self.assertEqual(52190, self.driver.earned_money)
        

if __name__ == "__main__":
    unittest.main()