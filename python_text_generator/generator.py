#!/usr/bin/env python

import sys
from python_text_generator.expression import split
from python_text_generator.evaluation import evaluate, execute, execute_init, default_scope
from python_text_generator.builtin import to_s

def generator(fin = sys.stdin, fout = sys.stdout):
    scope = default_scope()
    exec_code = []
    base_indent = [-1]

    execute_init(scope, fout)

    for line in fin.readlines():
        s = line.strip()
        if s.startswith("%"):
            if len(s) == 1 or s[1:].strip().startswith("#"):
                continue
            if len(exec_code) == 0:
                base_indent[0] = 1
                while s[base_indent[0]] in ' \t':
                    base_indent[0] += 1
            exec_code.append(s[base_indent[0]:])
            continue
        if len(exec_code) > 0:
            execute(exec_code, scope, fout)
            del exec_code[:]
        if len(s) == 0:
            fout.write("\n")
            continue

        sp_exprs = split(s)
        result = evaluate(sp_exprs, scope)

        fout.write("".join(map(to_s, result)))
        fout.write("\n")
    if len(exec_code) > 0:
        execute(exec_code, scope, fout)

