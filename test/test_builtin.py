import unittest
from src.main import generator
from StringIO import StringIO

class TestBuiltin(unittest.TestCase):
    def setUp(self):
        self.target = generator
        self.output = StringIO()

    def test_to_s(self):
        self.target(StringIO("to_s([1,2,3])"), self.output)
        self.assertEqual("1 2 3\n", self.output.getvalue())
        self.output.truncate(0)

    def test_to_s_with_single_delimiter(self):
        self.target(StringIO("to_s([1,2,3], '-')"), self.output)
        self.assertEqual("1-2-3\n", self.output.getvalue())
        self.output.truncate(0)

        self.target(StringIO("to_s([1,2,[3, 4, 4]], '-')"), self.output)
        self.assertEqual("1-2-3 4 4\n", self.output.getvalue())
        self.output.truncate(0)

        self.target(StringIO("to_s([1,2,3], '-=-')"), self.output)
        self.assertEqual("1-=-2-=-3\n", self.output.getvalue())

    def test_to_s_with_multi_delimiter(self):
        self.target(StringIO("to_s([1,2,3], ['-', '='])"), self.output)
        self.assertEqual("1-2-3\n", self.output.getvalue())
        self.output.truncate(0)

        self.target(StringIO("to_s([1,2,[3, 4, 4]], ['-', '='])"), self.output)
        self.assertEqual("1-2-3=4=4\n", self.output.getvalue())
        self.output.truncate(0)

        self.target(StringIO("to_s([1,2,[[3, 5, 6], 4, 4]], ['-', '='])"), self.output)
        self.assertEqual("1-2-3 5 6=4=4\n", self.output.getvalue())

    def test_to_s_with_empty_delimiter(self):
        self.target(StringIO("to_s([1,2,3], '')"), self.output)
        self.assertEqual("123\n", self.output.getvalue())

    def test_to_s_invalid_delimiter(self):
        self.assertRaises(TypeError, self.target, StringIO("to_s([1,2], 1)"), self.output)

