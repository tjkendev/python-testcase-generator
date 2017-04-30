#!/usr/bin/env python

import sys, os
import python_text_generator.setting as setting
import python_text_generator.builtin as builtin

def default_scope():
    return {
        'to_s': builtin.to_s
    }

def execute_init(scope, fout):
    fname = setting.init_pyfile
    if not os.path.isfile(fname):
        return

    f = open(fname, 'r')
    old_stdout, sys.stdout = sys.stdout, fout
    exec(f.read(), scope)
    sys.stdout = old_stdout
    f.close()

def execute(exec_code, scope, fout):
    old_stdout, sys.stdout = sys.stdout, fout
    exec("\n".join(exec_code), scope)
    sys.stdout = old_stdout

def evaluate(s_lst, scope):
    result = []
    for el in s_lst:
        if el in " \t":
            val = el
        else:
            val = eval(el, scope)
        if val is not None:
            result.append(val)
    return result
