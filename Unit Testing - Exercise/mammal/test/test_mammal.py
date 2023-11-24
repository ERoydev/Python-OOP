import unittest
from mammal.project.mammal import Mammal


class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.mammal = Mammal("Pegasus", "Horse", "Ihha")

    def test_initializing(self):
        self.assertEqual("Pegasus", self.mammal.name)
        self.assertEqual("Horse", self.mammal.type)
        self.assertEqual("Ihha", self.mammal.sound)
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_sound_func(self):
        result = self.mammal.make_sound()
        expected_result = f"Pegasus makes Ihha"
        self.assertEqual(expected_result, result)

    def test_get_kingdom_func(self):
        result = self.mammal.get_kingdom()
        expected_result = 'animals'
        self.assertEqual(expected_result, result)

    def test_info_func(self):
        result = self.mammal.info()
        expected_result = f"Pegasus is of type Horse"
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
