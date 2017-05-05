import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
from python_testcase_generator.generator import generator
from test.lib.IO import BaseIO

class TestSyntax(unittest.TestCase):
    def setUp(self):
        self.target = generator
        self.output = BaseIO()

    def test_tab_split(self):
        self.target(BaseIO("1\t2\t3"), self.output)
        self.assertEqual("1\t2\t3\n", self.output.getvalue())

    def test_skip_comment(self):
        self.target(BaseIO("1 2 3 [2] # comment"), self.output)
        self.assertEqual("1 2 3 2\n", self.output.getvalue())
        self.output.truncate(0)
        self.output.seek(0)

        self.target(BaseIO(" # comment"), self.output)
        self.assertEqual("\n", self.output.getvalue())
        self.output.truncate(0)
        self.output.seek(0)

        self.target(BaseIO("# comment ## comment"), self.output)
        self.assertEqual("\n", self.output.getvalue())

    def test_python_statement(self):
        self.target(BaseIO("% A = 1"), self.output)
        self.assertEqual("", self.output.getvalue())
        self.output.truncate(0)
        self.output.seek(0)

        self.target(BaseIO("% x = 1\nx x"), self.output)
        self.assertEqual("1 1\n", self.output.getvalue())
        self.output.truncate(0)
        self.output.seek(0)

        self.target(BaseIO("% print(1)"), self.output)
        self.assertEqual("1\n", self.output.getvalue())
        self.output.truncate(0)
        self.output.seek(0)

        self.target(BaseIO("%"), self.output)
        self.assertEqual("", self.output.getvalue())
