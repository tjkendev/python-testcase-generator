import unittest, platform
from python_testcase_generator.generator import generator
from test.lib.IO import BaseIO

class TestType(unittest.TestCase):
    def setUp(self):
        self.target = generator
        self.output = BaseIO()

    def test_type_int(self):
        self.target(BaseIO("1 2 3"), self.output)
        self.assertEqual("1 2 3\n", self.output.getvalue())

    def test_type_complex(self):
        self.target(BaseIO("1+1j 2+3j 3+1j"), self.output)
        self.assertEqual("(1+1j) (2+3j) (3+1j)\n", self.output.getvalue())

    def test_type_bool(self):
        self.target(BaseIO("True False 1==1 1!=1"), self.output)
        self.assertEqual("True False True False\n", self.output.getvalue())

    def test_type_str(self):
        self.target(BaseIO("'a' 'b' 'c'"), self.output)
        self.assertEqual("a b c\n", self.output.getvalue())

    def test_type_float(self):
        self.target(BaseIO("1.0 2.0 3. .1"), self.output)
        self.assertEqual("1.0 2.0 3.0 0.1\n", self.output.getvalue())

    @unittest.skipUnless(platform.python_version_tuple()[0] == '2', "unicode exists only in Python2")
    def test_type_unicode(self):
        self.target(BaseIO("unicode('ab') u'b'"), self.output)
        self.assertEqual("ab b\n", self.output.getvalue())

    @unittest.skipUnless(platform.python_version_tuple()[0] == '2', "This test only in Python2")
    def test_type_bytes_2(self):
        self.target(BaseIO("bytes('a') b'b'"), self.output)
        self.assertEqual("a b\n", self.output.getvalue())

    @unittest.skipUnless(platform.python_version_tuple()[0] == '3', "This test only in Python3")
    def test_type_bytes_3(self):
        self.target(BaseIO("'ab'.encode('utf-8') b'b'"), self.output)
        self.assertEqual("ab b\n", self.output.getvalue())

    def test_type_None(self):
        self.target(BaseIO("None None"), self.output)
        self.assertEqual(" \n", self.output.getvalue())
