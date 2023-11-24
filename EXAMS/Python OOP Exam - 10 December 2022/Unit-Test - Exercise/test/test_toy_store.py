from project.toy_store import ToyStore
import unittest


class SimpleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.toy = ToyStore()

    def test_initialization_if_correct(self):
        self.assertEqual({"A": None,"B": None,"C": None, "D": None,"E": None,"F": None,"G": None,}, self.toy.toy_shelf)

    def test_add_toy_if_shelf_not_in_toy_shelf_exception(self):
        for word in ["K", "L", "M", "O"]:
            with self.assertRaises(Exception) as ex:
                self.toy.add_toy(word, "mickey")

            self.assertEqual("Shelf doesn't exist!", str(ex.exception))

        for word in ["A", "B", "C", "D", "E", "F", "G"]:
            result = self.toy.add_toy(word, 'mickey')
            self.assertNotEqual("Shelf doesn't exist!", result)

    def test_add_toy_if_toy_exists_in_existing_shelf_exception(self):
        self.toy.toy_shelf['A'] = 'mickey'

        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("A", 'mickey')

        self.assertEqual("Toy is already in shelf!", str(ex.exception))
        self.toy.add_toy("B", 'mouse')
        self.assertEqual({'A': 'mickey', 'B': 'mouse', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}, self.toy.toy_shelf)

    def test_add_toy_if_shelf_is_already_taken_exception(self):
        self.toy.toy_shelf['A'] = 'mickey'

        with self.assertRaises(Exception) as ex:
            self.toy.add_toy('A', 'mouse')

        self.assertEqual("Shelf is already taken!", str(ex.exception))
        self.toy.add_toy('B', 'mouse')
        self.assertEqual({'A': 'mickey', 'B': 'mouse', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}, self.toy.toy_shelf)

    def test_add_toy_if_shelf_exist_but_its_empty(self):
        self.assertEqual({'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}, self.toy.toy_shelf)
        result = self.toy.add_toy("A", 'mickey')
        self.assertEqual(f"Toy:mickey placed successfully!", result)
        self.assertEqual({'A': 'mickey', 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}, self.toy.toy_shelf)

    def test_remove_toy_if_shelf_doesnt_exists_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy("H", 'mouse')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy("O", 'mouse')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_toy_dont_exist_in_existing_shelf_exception(self):
        self.toy.toy_shelf['B'] = 'mouse'
        self.toy.toy_shelf['C'] = ('something')

        for word in ["A", "B", "C", "D", "E", "F", "G"]:
            with self.assertRaises(Exception) as ex:
                self.toy.remove_toy(word, 'mickey')

            self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_if_toy_is_removed_correctly_from_shelf(self):
        self.toy.toy_shelf['A'] = 'mickey'
        self.toy.toy_shelf['B'] = 'mouse'

        self.assertEqual('mickey', self.toy.toy_shelf['A'])
        self.assertEqual('mouse', self.toy.toy_shelf['B'])

        result1 = self.toy.remove_toy('A', 'mickey')
        result2 = self.toy.remove_toy('B', 'mouse')

        self.assertEqual(None, self.toy.toy_shelf['A'])
        self.assertEqual(None, self.toy.toy_shelf['B'])

        self.assertEqual(f"Remove toy:mickey successfully!", result1)
        self.assertEqual(f"Remove toy:mouse successfully!", result2)


if __name__ == "__main__":
    unittest.main()