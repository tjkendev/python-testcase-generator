import unittest
from src.generator import generator
from io import BytesIO

class TestQuotes(unittest.TestCase):
    def setUp(self):
        self.target = generator
        self.output = BytesIO()

    def test_single_quotes(self):
        self.target(BytesIO('\'abc "123" d d a\''), self.output)
        self.assertEqual('abc "123" d d a\n', self.output.getvalue())

    def test_nested_single_quotes(self):
        self.target(BytesIO('\'abc \\\'123\\\' d d a\''), self.output)
        self.assertEqual('abc \'123\' d d a\n', self.output.getvalue())

    def test_double_quotes(self):
        self.target(BytesIO('"abc \'123\' d d a"'), self.output)
        self.assertEqual('abc \'123\' d d a\n', self.output.getvalue())

    def test_nested_double_quotes(self):
        self.target(BytesIO('"abc \\"123\\" d d a"'), self.output)
        self.assertEqual('abc "123" d d a\n', self.output.getvalue())

    def test_back_quotes(self):
        self.target(BytesIO('` 1 + 2 * 3 `'), self.output)
        self.assertEqual('7\n', self.output.getvalue())

    def test_nested_back_quotes(self):
        self.target(BytesIO('` "`aiueo`" `'), self.output)
        self.assertEqual('`aiueo`\n', self.output.getvalue())
        self.output.truncate(0)
        self.output.seek(0)

        self.target(BytesIO('` \'`aiueo`\' `'), self.output)
        self.assertEqual('`aiueo`\n', self.output.getvalue())
