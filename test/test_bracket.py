import unittest
from python_text_generator_tool.main import generator
from StringIO import StringIO

class TestBracket(unittest.TestCase):
    def setUp(self):
        self.target = generator
        self.output = StringIO()

    def test_brackets_list(self):
        self.target(StringIO("[1, 2, 3]"), self.output)
        self.assertEqual("1 2 3\n", self.output.getvalue())

    def test_brackets_nested_list(self):
        self.target(StringIO("[1, [4, [5, 6]], 3]"), self.output)
        self.assertEqual("1 4 5 6 3\n", self.output.getvalue())

    def test_brackets_generator_list(self):
        self.target(StringIO("[i**2 for i in range(4)]"), self.output)
        self.assertEqual("0 1 4 9\n", self.output.getvalue())

    def test_brackets_caluculate_list(self):
        self.target(StringIO("[7]+[1, 2]*2+[6]"), self.output)
        self.assertEqual("7 1 2 1 2 6\n", self.output.getvalue())

    def test_brackets_array_ref(self):
        self.target(StringIO("[1, 2, 3][ 1 ]"), self.output)
        self.assertEqual("2\n", self.output.getvalue())

    def test_brackets_in_string(self):
        self.target(StringIO("[1, '] [', 3]"), self.output)
        self.assertEqual("1 ] [ 3\n", self.output.getvalue())

    def test_parenthesis_tuple(self):
        self.target(StringIO("(1, 2, 3)"), self.output)
        self.assertEqual("1 2 3\n", self.output.getvalue())

    def test_parenthesis_nested_tuple(self):
        self.target(StringIO("(1, (4, (5, 6)), 3)"), self.output)
        self.assertEqual("1 4 5 6 3\n", self.output.getvalue())

    def test_parenthesis_function_call(self):
        self.target(StringIO("round( 1.8 )"), self.output)
        self.assertEqual("2.0\n", self.output.getvalue())

    def test_parenthesis_generator(self):
        self.target(StringIO("(i**2 for i in range(4))"), self.output)
        self.assertEqual("0 1 4 9\n", self.output.getvalue())

    def test_parenthesis_in_string(self):
        self.target(StringIO("(1, ') (', 3)"), self.output)
        self.assertEqual("1 ) ( 3\n", self.output.getvalue())

    def test_brace_set(self):
        self.target(StringIO("{1, 2, 3}"), self.output)
        self.assertEqual("1 2 3\n", self.output.getvalue())

    def test_brace_dict(self):
        self.target(StringIO("{1: 2, 3: 4}"), self.output)
        self.assertEqual("1 3\n", self.output.getvalue())

    def test_brace_generator_set(self):
        self.target(StringIO("{i**2 for i in range(4)}"), self.output)
        self.assertEqual("0 1 4 9\n", self.output.getvalue())

    def test_brace_set_in_string(self):
        self.target(StringIO("{1, 3, '} {'}"), self.output)
        self.assertEqual("1 3 } {\n", self.output.getvalue())

    def test_mixed_nested_bracket(self):
        self.target(StringIO("(1, [4, {6}, (5, 8)], 3)"), self.output)
        self.assertEqual("1 4 6 5 8 3\n", self.output.getvalue())

