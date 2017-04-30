
import unittest
from src.generator import generator
from io import BytesIO

class TestSyntax(unittest.TestCase):
    def setUp(self):
        self.target = generator
        self.output = BytesIO()

    def test_tab_split(self):
        self.target(BytesIO("1\t2\t3"), self.output)
        self.assertEqual("1\t2\t3\n", self.output.getvalue())

    def test_skip_comment(self):
        self.target(BytesIO("1 2 3 [2] # comment"), self.output)
        self.assertEqual("1 2 3 2\n", self.output.getvalue())
        self.output.truncate(0)
        self.output.seek(0)

        self.target(BytesIO(" # comment"), self.output)
        self.assertEqual("\n", self.output.getvalue())
        self.output.truncate(0)
        self.output.seek(0)

        self.target(BytesIO("# comment ## comment"), self.output)
        self.assertEqual("\n", self.output.getvalue())

    def test_python_statement(self):
        self.target(BytesIO("% A = 1"), self.output)
        self.assertEqual("", self.output.getvalue())
        self.output.truncate(0)
        self.output.seek(0)

        self.target(BytesIO("% x = 1\nx x"), self.output)
        self.assertEqual("1 1\n", self.output.getvalue())
        self.output.truncate(0)
        self.output.seek(0)

        self.target(BytesIO("% print(1)"), self.output)
        self.assertEqual("1\n", self.output.getvalue())
        self.output.truncate(0)
        self.output.seek(0)

        self.target(BytesIO("%"), self.output)
        self.assertEqual("", self.output.getvalue())
