#!/usr/bin/env python
import collections

def to_s(val, delimiter=None):
    if delimiter is None:
        delimiter = ' '
    if type(delimiter) == str:
        delimiter = [delimiter]
    c_delimiter = delimiter[0]
    result = []
    if len(delimiter) <= 1:
        n_delimiter = [' ']
    else:
        n_delimiter = delimiter[1:]
    if (isinstance(val, collections.Iterable) and not isinstance(val, basestring)):
        return c_delimiter.join(map(lambda x: to_s(x, n_delimiter), val))
    return str(val)
