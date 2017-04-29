
import unittest
from src.generator import generator
from StringIO import StringIO

class TestSyntax(unittest.TestCase):
    def setUp(self):
        self.target = generator
        self.output = StringIO()

    def test_tab_split(self):
        self.target(StringIO("1\t2\t3"), self.output)
        self.assertEqual("1\t2\t3\n", self.output.getvalue())

    def test_skip_comment(self):
        self.target(StringIO("1 2 3 [2] # comment"), self.output)
        self.assertEqual("1 2 3 2\n", self.output.getvalue())
        self.output.truncate(0)

        self.target(StringIO(" # comment"), self.output)
        self.assertEqual("\n", self.output.getvalue())
        self.output.truncate(0)

        self.target(StringIO("# comment ## comment"), self.output)
        self.assertEqual("\n", self.output.getvalue())

    def test_python_statement(self):
        self.target(StringIO("% A = 1"), self.output)
        self.assertEqual("", self.output.getvalue())
        self.output.truncate(0)

        self.target(StringIO("% x = 1\nx x"), self.output)
        self.assertEqual("1 1\n", self.output.getvalue())
        self.output.truncate(0)

        self.target(StringIO("% print(1)"), self.output)
        self.assertEqual("1\n", self.output.getvalue())
        self.output.truncate(0)

        self.target(StringIO("%"), self.output)
        self.assertEqual("", self.output.getvalue())
