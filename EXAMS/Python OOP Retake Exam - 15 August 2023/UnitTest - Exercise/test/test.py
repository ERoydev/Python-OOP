from project.trip import Trip
import unittest


class SimpleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.trip = Trip(1000, 123, True)

    def test_class_attribute(self):
        self.assertEqual({'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}, self.trip.DESTINATION_PRICES_PER_PERSON)

    def test_initialization(self):
        self.assertEqual(1000, self.trip.budget)
        self.assertEqual(123, self.trip.travelers)
        self.assertEqual(True, self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_travelers_property(self):
        result = self.trip.travelers
        self.assertEqual(123, result)
        self.assertEqual(123, self.trip.travelers)

    def test_travelers_setter_if_value_less_than_1_exception(self):
        for i in range(0, -5, -1):
            with self.assertRaises(ValueError) as ex:
                self.trip.travelers = i

            self.assertEqual('At least one traveler is required!', str(ex.exception))

        self.trip.travelers = 1
        self.assertEqual(1, self.trip.travelers)

    def test_travelers_setter_if_value_is_correct(self):
        for i in range(1, 10):
            result = self.trip.travelers = i
            self.assertEqual(i, result)
            self.assertEqual(i, self.trip.travelers)

    def test_is_family_property(self):
        result = self.trip.is_family
        self.assertEqual(True, result)
        self.assertEqual(True, self.trip.is_family)

    def test_is_family_setter_if_value_exist_and_travelers_less_than_2(self):
        for i in range(1, 2):
            self.trip.travelers = i
            self.trip.is_family = True
            self.assertFalse(self.trip.is_family)

        self.trip.travelers = 2
        self.trip.is_family = True
        self.assertTrue(self.trip.is_family)

        self.trip.travelers = 3
        self.trip.is_family = False
        self.assertFalse(self.trip.is_family)

    def test_book_a_trip_if_destination_not_in_class_attribute_property(self):
        self.assertEqual({'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}, self.trip.DESTINATION_PRICES_PER_PERSON)

        result = self.trip.book_a_trip('Romania')
        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

        result = self.trip.book_a_trip('Italy')
        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

        result = self.trip.book_a_trip('Chinese')
        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

        result = self.trip.book_a_trip('England')
        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

    def test_book_a_trip_required_price_if_budget_is_not_enough(self):
        self.assertEqual({'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500},
                         self.trip.DESTINATION_PRICES_PER_PERSON)

        # equal
        self.trip.budget = 500
        self.trip.travelers = 1
        self.trip.is_family = False
        result = self.trip.book_a_trip('Bulgaria')
        self.assertNotEqual('Your budget is not enough!', result)
        self.assertEqual(0, self.trip.budget)
        self.assertEqual({'Bulgaria': 500}, self.trip.booked_destinations_paid_amounts)

        # less than budget
        self.trip.budget = 501
        self.trip.travelers = 1
        self.trip.is_family = False
        result = self.trip.book_a_trip('Bulgaria')
        self.assertNotEqual('Your budget is not enough!', result)
        self.assertEqual(1, self.trip.budget)
        self.assertEqual({'Bulgaria': 500}, self.trip.booked_destinations_paid_amounts)

        # budget is less than required price
        self.trip.travelers = 3
        self.trip.budget = 1000
        self.trip.is_family = True
        self.trip.booked_destinations_paid_amounts = {}
        result = self.trip.book_a_trip('Bulgaria')
        self.assertEqual('Your budget is not enough!', result)
        self.assertEqual(1000, self.trip.budget)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

        # budget is less than required price
        self.trip.booked_destinations_paid_amounts = {}
        self.trip.travelers = 3
        self.trip.budget = 1000
        self.trip.is_family = False
        result = self.trip.book_a_trip('Bulgaria')
        self.assertEqual('Your budget is not enough!', result)
        self.assertEqual(1000, self.trip.budget)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_book_a_trip(self):
        self.assertEqual({'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500},
                         self.trip.DESTINATION_PRICES_PER_PERSON)

        self.trip.travelers = 1
        self.trip.budget = 500
        self.trip.is_family = False

        result = self.trip.book_a_trip('Bulgaria')
        self.assertEqual(0, self.trip.budget)
        self.assertEqual({'Bulgaria': 500}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 0.00', result)

        self.trip.travelers = 2
        self.trip.budget = 13000
        self.trip.is_family = True

        result = self.trip.book_a_trip('Brazil')
        self.assertEqual(1840, self.trip.budget)
        self.assertEqual({'Bulgaria': 500, 'Brazil': 11160}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(f'Successfully booked destination Brazil! Your budget left is 1840.00', result)

        self.trip.travelers = 1
        self.trip.budget = 6400
        self.trip.is_family = True
        result = self.trip.book_a_trip('Brazil')
        self.assertEqual(200, self.trip.budget)
        self.assertEqual({'Bulgaria': 500, 'Brazil': 6200}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(f'Successfully booked destination Brazil! Your budget left is 200.00', result)

    def test_booking_status_if_not_bookings_yet_raises(self):
        self.trip.booked_destinations_paid_amounts = {}
        result = self.trip.booking_status()
        self.assertEqual(f'No bookings yet. Budget: 1000.00', result)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(1000, self.trip.budget)

    def test_booking_status_with_bookings_maked(self):
        self.trip.budget = 500
        self.trip.booked_destinations_paid_amounts = {'Bulgaria': 500, 'Brazil': 6200}
        self.trip.travelers = 2

        expected_result = f"Booked Destination: Brazil\nPaid Amount: 6200.00\nBooked Destination: Bulgaria\nPaid Amount: 500.00\nNumber of Travelers: 2\nBudget Left: 500.00"
        result = self.trip.booking_status()
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()

