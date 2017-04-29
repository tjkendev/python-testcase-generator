import unittest
from python_text_generator_tool.main import generator
from StringIO import StringIO

class TestQuotes(unittest.TestCase):
    def setUp(self):
        self.target = generator
        self.output = StringIO()

    def test_single_quotes(self):
        self.target(StringIO('\'abc "123" d d a\''), self.output)
        self.assertEqual('abc "123" d d a\n', self.output.getvalue())

    def test_nested_single_quotes(self):
        self.target(StringIO('\'abc \\\'123\\\' d d a\''), self.output)
        self.assertEqual('abc \'123\' d d a\n', self.output.getvalue())

    def test_double_quotes(self):
        self.target(StringIO('"abc \'123\' d d a"'), self.output)
        self.assertEqual('abc \'123\' d d a\n', self.output.getvalue())

    def test_nested_double_quotes(self):
        self.target(StringIO('"abc \\"123\\" d d a"'), self.output)
        self.assertEqual('abc "123" d d a\n', self.output.getvalue())

    def test_back_quotes(self):
        self.target(StringIO('` 1 + 2 * 3 `'), self.output)
        self.assertEqual('7\n', self.output.getvalue())

    def test_nested_back_quotes(self):
        self.target(StringIO('` "`aiueo`" `'), self.output)
        self.assertEqual('`aiueo`\n', self.output.getvalue())
        self.output.truncate(0)

        self.target(StringIO('` \'`aiueo`\' `'), self.output)
        self.assertEqual('`aiueo`\n', self.output.getvalue())
