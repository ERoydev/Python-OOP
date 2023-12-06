import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):

    def setUp(self) -> None:
        self.cl = CustomList(5, 'asd', 3.8)

    def test_initialize(self):
        cl = CustomList()
        self.assertEqual(cl._CustomList__values, [])

        cl = CustomList(5, 'asd', 3.8)
        self.assertEqual(cl._CustomList__values, [5, 'asd', 3.8])

    def test_append_passed_argument_raises(self):

        with self.assertRaises(TypeError) as ex:
            self.cl.append()

        self.assertIn("missing 1 required positional argument", str(ex.exception))

    def test_append_add_to_last_index_in_list(self):
        #Preparation
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        #Execute
        result = self.cl.append(5)

        self.assertEqual(self.cl._CustomList__values[-1], 5)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8, 5])
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, result)

    def test_append_element_to_empty_list(self):
        new_list = CustomList()
        self.assertEqual(new_list._CustomList__values, [])

        new_list.append(3)

        self.assertEqual(new_list._CustomList__values, [3])

    def test_remove_passed_argument_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.cl.remove()

        self.assertIn('missing 1 required positional argument', str(ex.exception))

    def test_remove_if_index_out_of_range_exception(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)

        for index in range(3, 5):
            with self.assertRaises(IndexError) as ex:
                self.cl.remove(index)

            self.assertEqual('List index out of range', str(ex.exception))

    def test_remove_if_removed_the_correct_index(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        result = self.cl.remove(1)
        self.assertEqual(self.cl._CustomList__values, [5, 3.8])
        self.assertEqual(len(self.cl._CustomList__values), 2)
        self.assertEqual('asd', result)

        result = self.cl.remove(0)
        self.assertEqual(self.cl._CustomList__values, [3.8])
        self.assertEqual(len(self.cl._CustomList__values), 1)
        self.assertEqual(5, result)

    def test_remove_if_list_is_empty(self):
        new = CustomList()
        with self.assertRaises(IndexError) as ex:
            new.remove(0)

        self.assertEqual('List index out of range', str(ex.exception))

    def test_get_passed_arguments_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.cl.get()

        self.assertIn('missing 1 required positional argument', str(ex.exception))

    def test_get_if_index_out_of_range_exception(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)

        for index in range(3, 6):
            with self.assertRaises(IndexError) as ex:
                self.cl.get(index)

            self.assertEqual('List index out of range', str(ex.exception))

        self.assertEqual(len(self.cl._CustomList__values), 3)

    def test_get_if_i_get_correct_value_correspond_to_index(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)

        for index in range(0, 3):
            result = self.cl.get(index)

            self.assertEqual(self.cl._CustomList__values[index], result)

    def test_get_if_list_is_empty(self):
        new = CustomList()

        with self.assertRaises(IndexError) as ex:
            new.get(0)

        self.assertEqual('List index out of range', str(ex.exception))

    def test_extend_passed_arguments_raises(self):

        with self.assertRaises(TypeError) as ex:
            self.cl.extend()

        self.assertIn('missing 1 required positional argument', str(ex.exception))

    def test_extend(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        result = self.cl.extend(1, 2, 3)

        self.assertEqual(len(self.cl._CustomList__values), 6)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8, 1, 2, 3])

        self.assertEqual(self.cl._CustomList__values, result)

    def test_insert_parameters_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.cl.insert()

        self.assertIn('missing 2 required positional arguments', str(ex.exception))

        with self.assertRaises(TypeError) as ex:
            self.cl.insert(3)

        self.assertIn('missing 1 required positional argument', str(ex.exception))

        with self.assertRaises(TypeError) as ex:
            self.cl.insert(2, 3, 4)

        self.assertIn('takes 3 positional arguments but 4 were given', str(ex.exception))

    def test_insert_value_put_on_correct_index(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        result = self.cl.insert(4, 55)

        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8, 55])
        self.assertEqual([5, 'asd', 3.8, 55], result)

        result = self.cl.insert(0, 12)

        self.assertEqual(len(self.cl._CustomList__values), 5)
        self.assertEqual(self.cl._CustomList__values, [12, 5, 'asd', 3.8, 55])
        self.assertEqual([12, 5, 'asd', 3.8, 55], result)

        result = self.cl.insert(1, 'ds')

        self.assertEqual(len(self.cl._CustomList__values), 6)
        self.assertEqual(self.cl._CustomList__values, [12,'ds', 5, 'asd', 3.8, 55])
        self.assertEqual([12,'ds', 5, 'asd', 3.8, 55], result)

    def test_pop_if_list_is_empty_exception(self):
        new_list = CustomList()

        with self.assertRaises(IndexError) as ex:
            new_list.pop()

        self.assertEqual('pop from empty list', str(ex.exception))

    def test_pop_if_removed_correct_value(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        result = self.cl.pop()
        self.assertEqual(3.8, result)
        self.assertEqual(len(self.cl._CustomList__values), 2)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd'])

        result = self.cl.pop()
        self.assertEqual('asd', result)
        self.assertEqual(len(self.cl._CustomList__values), 1)
        self.assertEqual(self.cl._CustomList__values, [5])

    def test_clear(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        self.cl.clear()
        self.assertEqual(self.cl._CustomList__values, [])

    def test_index_if_arguments_are_not_passed_raises(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        with self.assertRaises(TypeError) as ex:
            self.cl.index()

        self.assertIn('missing 1 required positional argument', str(ex.exception))

    def test_index_if_value_is_not_in_list_exception(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        result = self.cl.index('ada')
        self.assertEqual('ada is not in list', result)

        result = self.cl.index(2)
        self.assertEqual('2 is not in list', result)

        result = self.cl.index('kolio')
        self.assertEqual('kolio is not in list', result)

    def test_index_if_return_correct_index(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        result = self.cl.index(3.8)
        self.assertEqual(2, result)

        result = self.cl.index('asd')
        self.assertEqual(1, result)

        result = self.cl.index(5)
        self.assertEqual(0, result)

    def test_count(self):
        self.cl.append('asd')
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8, 'asd'])

        result = self.cl.count(5)
        self.assertEqual(1, result)

        result = self.cl.count('asd')
        self.assertEqual(2, result)

        result = self.cl.count(6)
        self.assertEqual(0, result)

    def test_count_if_argument_not_passed_exception(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        with self.assertRaises(TypeError) as ex:
            self.cl.count()

        self.assertIn('missing 1 required positional argument', str(ex.exception))

    def test_reverse_returns_reverse_list_values(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        result = self.cl.reverse()
        self.assertEqual([3.8, 'asd', 5], result)
        self.assertEqual(len(self.cl._CustomList__values), 3)

        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

    def test_copy_returns_copy_of_the_list(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        result = self.cl.copy()

        self.assertNotEqual(id(self.cl._CustomList__values), id(result))
        self.assertEqual([5, 'asd', 3.8], result)

    def test_copy_references_if_are_copied_too(self):
        self.cl.append([1, 2, 3])
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8, [1, 2, 3]])

        result = self.cl.copy()

        self.assertNotEqual(id(self.cl._CustomList__values), id(result))
        self.assertEqual([5, 'asd', 3.8, [1, 2, 3]], result)

        last_ref_el = self.cl._CustomList__values[-1]

        self.assertEqual([1, 2, 3], last_ref_el)
        self.assertNotEqual(id(last_ref_el), id(result[-1]))

    def test_size(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        result = self.cl.size()
        self.assertEqual(3, result)

        self.cl.append('kako')

        result = self.cl.size()
        self.assertEqual(4, result)

    def test_add_first(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        self.cl.add_first('kolio')

        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, ['kolio', 5, 'asd', 3.8])

    def test_dictionize(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        result = self.cl.dictionize()
        self.assertEqual({5: 'asd', 3.8: " "}, result)

        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        self.cl.append(15)
        result = self.cl.dictionize()
        self.assertEqual({5: 'asd', 3.8: 15}, result)

        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8, 15])

    def test_move(self):
        self.cl.append(100)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8, 100])

        result = self.cl.move(2)

        self.assertEqual([3.8, 100, 5, 'asd'], result)

        result = self.cl.move(5)
        self.assertEqual([3.8, 100, 5, 'asd'], result)

        result = self.cl.move(3)
        self.assertEqual(['asd', 3.8, 100, 5], result)

        self.assertEqual(len(self.cl._CustomList__values), 4)

    def test_move_invalid_amount_type(self):
        with self.assertRaises(ValueError) as ex:
            self.cl.move('asda')

        self.assertEqual('Amount should be integer!', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.cl.move([12, 3])

        self.assertEqual('Amount should be integer!', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.cl.move({})

        self.assertEqual('Amount should be integer!', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.cl.move(())

        self.assertEqual('Amount should be integer!', str(ex.exception))

    def test_move_invalid_amount(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        with self.assertRaises(ValueError) as ex:
            self.cl.move(-1)

        self.assertEqual('Cannot move a negative amount!', str(ex.exception))

        result = self.cl.move(0)
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, 'asd', 3.8], result)

    def test_sum_with_string_in_list(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        result = self.cl.sum()
        self.assertEqual(11.8, result)

    def test_sum_with_collection_in_list(self):
        new = CustomList()
        self.cl._CustomList__values = [1, 2, [3, 4, 5], 10]

        result = self.cl.sum()
        self.assertEqual(16, result)

        self.cl._CustomList__values = [1, 2, (3, 4, 5), 10]
        result = self.cl.sum()
        self.assertEqual(16, result)

    def test_sum_with_only_numbers(self):
        new = CustomList()
        self.cl._CustomList__values = [1, 2, 10]

        result = self.cl.sum()

        self.assertEqual(13, result)

    def test_overbound(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        result = self.cl.overbound()
        self.assertEqual(5, result)

        self.cl.append('adwsdwsawd')
        result = self.cl.overbound()
        self.assertEqual(10, result)

    def test_underbound(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 'asd', 3.8])

        result = self.cl.underbound()
        self.assertEqual(3, result)

        self.cl.append('adwsdwsawd')
        result = self.cl.underbound()
        self.assertEqual(3, result)


if __name__ == "__main__":
    unittest.main()
