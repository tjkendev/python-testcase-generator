import platform
from io import StringIO, BytesIO

# String IO supporting "str" is difference between Python2 and Python3.
# Python2: StringIO => unicode     , BytesIO => str
# Python3: StringIO => str(unicode), BytesIO => bytes
version = platform.python_version_tuple()
if version[0] == '2':
    BaseIO = BytesIO
elif version[0] == '3':
    BaseIO = StringIO
