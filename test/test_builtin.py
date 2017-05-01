import unittest
from python_testcase_generator.builtin import to_s

class TestBuiltin(unittest.TestCase):

    def test_to_s(self):
        result = to_s([1, 2, 3])
        self.assertEqual("1 2 3", result)

    def test_to_s_with_single_delimiter(self):
        result = to_s([1, 2, 3], '-')
        self.assertEqual("1-2-3", result)

        result = to_s([1, 2, [3, 4, 4]], '-')
        self.assertEqual("1-2-3 4 4", result)

        result = to_s([1, 2, 3], '-=-')
        self.assertEqual("1-=-2-=-3", result)

    def test_to_s_with_multi_delimiter(self):
        result = to_s([1, 2, 3], ['-', '='])
        self.assertEqual("1-2-3", result)

        result = to_s([1,2,[3, 4, 4]], ['-', '='])
        self.assertEqual("1-2-3=4=4", result)

        result = to_s([1,2,[[3, 5, 6], 4, 4]], ['-', '='])
        self.assertEqual("1-2-3 5 6=4=4", result)

    def test_to_s_with_empty_delimiter(self):
        result = to_s([1,2,3], '')
        self.assertEqual("123", result)
