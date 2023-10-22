class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTest(TestCase):

    def test_is_initialized_correctly_without_data(self):
        integer = IntegerList()
        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_correctly_with_wrong_data(self):
        integer = IntegerList("asd", 5.6, 10.2)
        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_with_correct_data(self):
        integer = IntegerList(4, 5, 6, 2)
        self.assertEqual([4, 5, 6, 2], integer._IntegerList__data)

    def test_is_get_data_return_list(self):
        integer = IntegerList()
        result = integer.get_data()

        self.assertEqual([], result)

    def test_add_method_with_string_to_return_ValueError(self):
        integer = IntegerList()

        with self.assertRaises(ValueError) as ex:
            integer.add("asd")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_method_with_float_to_return_ValueError(self):
        integer = IntegerList()

        with self.assertRaises(ValueError) as ex:
            integer.add(4.2)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_method_if_add_element_to_list(self):
        integer = IntegerList(3, 4, 5)

        integer.add(3)

        self.assertEqual([3, 4, 5, 3], integer._IntegerList__data)

    def test_add_method_if_return_value(self):
        integer = IntegerList(3, 4, 5)

        result = integer.add(3)

        self.assertEqual([3, 4, 5, 3], result)

    def test_remove_index_with_equal_index(self):
        integer = IntegerList(1, 2)

        with self.assertRaises(IndexError) as ex:
            integer.remove_index(2)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_with_larger_index(self):
        integer = IntegerList(1, 2)

        with self.assertRaises(IndexError) as ex:
            integer.remove_index(3)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_if_delete_correct_value(self):
        integer = IntegerList(1, 2, 3)

        integer.remove_index(1)
        self.assertEqual([1, 3], integer._IntegerList__data)
        integer.remove_index(1)
        self.assertEqual([1], integer._IntegerList__data)

    def test_remove_index_if_return_removed_element(self):
        integer = IntegerList(1, 2, 3)

        result = integer.remove_index(1)
        self.assertEqual(2, result)

    def test_get_method_with_equal_index(self):
        integer = IntegerList(1, 2, 3)

        with self.assertRaises(IndexError) as ex:
            integer.get(3)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_method_with_larger_index(self):
        integer = IntegerList(1, 2, 3)

        with self.assertRaises(IndexError) as ex:
            integer.get(4)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_method_if_return_accessed_element(self):
        integer = IntegerList(1, 2, 3)

        result = integer.get(2)

        self.assertEqual(3, result)

    def test_insert_with_equal_index(self):
        integer = IntegerList(1, 2, 3)

        with self.assertRaises(IndexError) as ex:
            integer.insert(3, 1)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_with_larger_index(self):
        integer = IntegerList(1, 2, 3)

        with self.assertRaises(IndexError) as ex:
            integer.insert(4, 1)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_with_string_element(self):
        integer = IntegerList(1, 2, 3)

        with self.assertRaises(ValueError) as ex:
            integer.insert(2, "abc")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_with_float_element(self):
        integer = IntegerList(1, 2, 3)

        with self.assertRaises(ValueError) as ex:
            integer.insert(2, 3.4)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_with_correct_data(self):
        integer = IntegerList(1, 2, 3)

        integer.insert(2, 7)

        self.assertEqual([1, 2, 7, 3], integer._IntegerList__data)

    def test_get_biggest_return_correct_element(self):
        integer = IntegerList(1, 2, 3)

        result = integer.get_biggest()

        self.assertEqual(3, result)

    def test_get_index_return(self):
        integer = IntegerList(1, 2, 3)

        result = integer.get_index(2)

        self.assertEqual(1, result)


if __name__ == "__main__":
    main()