#!/usr/bin/env python

import sys

def execute(exec_code, scope, fout):
    old_stdout, sys.stdout = sys.stdout, fout
    exec("\n".join(exec_code), scope)
    sys.stdout = old_stdout

def evaluate(s_lst, scope):
    result = []
    for el in s_lst:
        if el == " ":
            val = el
        else:
            val = eval(el, scope)
        if val is not None:
            result.append(val)
    return result
