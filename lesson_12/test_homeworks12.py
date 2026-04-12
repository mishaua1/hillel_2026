import unittest
from homeworks import sum_even
from homeworks import filter_strings
from homeworks import contains_h
from homeworks import check_age

class TestSumEven(unittest.TestCase):

    def test_basic(self):
        result = sum_even([1, 2, 3, 4])
        self.assertEqual(result, 6)

    def test_all_even(self):
        result = sum_even([2, 4, 6])
        self.assertEqual(result, 12)

    def test_no_even(self):
        result = sum_even([1, 3, 5])
        self.assertEqual(result, 0)

    def test_empty(self):
        result = sum_even([])
        self.assertEqual(result, 0)


class TestFilterStrings(unittest.TestCase):

    def test_basic(self):
        result = filter_strings([1, 'hello', True, 'world'])
        self.assertEqual(result, ['hello', 'world'])

    def test_no_strings(self):
        result = filter_strings([1, 2, 3])
        self.assertEqual(result, [])

    def test_empty(self):
        result = filter_strings([])
        self.assertEqual(result, [])

class TestContainsH(unittest.TestCase):

    def test_lowercase_h(self):
        result = contains_h("hello")
        self.assertTrue(result)

    def test_uppercase_h(self):
        result = contains_h("Hello")
        self.assertTrue(result)

    def test_no_h(self):
        result = contains_h("world")
        self.assertFalse(result)

class TestСheck_Аge(unittest.TestCase):

    def test_age_passes(self):
        lst = [('Alice', 'Smith', 35)]
        result = check_age(lst, [0], 30)
        self.assertTrue(result)

    def test_age_fails(self):
        lst = [('Alice', 'Smith', 25)]
        result = check_age(lst, [0], 30)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main(verbosity=2)
