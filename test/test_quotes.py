import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
from python_testcase_generator.generator import generator
from test.lib.IO import BaseIO

class TestQuotes(unittest.TestCase):
    def setUp(self):
        self.target = generator
        self.output = BaseIO()

    def test_single_quotes(self):
        self.target(BaseIO('\'abc "123" d d a\''), self.output)
        self.assertEqual('abc "123" d d a\n', self.output.getvalue())

    def test_nested_single_quotes(self):
        self.target(BaseIO('\'abc \\\'123\\\' d d a\''), self.output)
        self.assertEqual('abc \'123\' d d a\n', self.output.getvalue())

    def test_double_quotes(self):
        self.target(BaseIO('"abc \'123\' d d a"'), self.output)
        self.assertEqual('abc \'123\' d d a\n', self.output.getvalue())

    def test_nested_double_quotes(self):
        self.target(BaseIO('"abc \\"123\\" d d a"'), self.output)
        self.assertEqual('abc "123" d d a\n', self.output.getvalue())

    def test_back_quotes(self):
        self.target(BaseIO('` 1 + 2 * 3 `'), self.output)
        self.assertEqual('7\n', self.output.getvalue())

    def test_nested_back_quotes(self):
        self.target(BaseIO('` "`aiueo`" `'), self.output)
        self.assertEqual('`aiueo`\n', self.output.getvalue())
        self.output.truncate(0)
        self.output.seek(0)

        self.target(BaseIO('` \'`aiueo`\' `'), self.output)
        self.assertEqual('`aiueo`\n', self.output.getvalue())
