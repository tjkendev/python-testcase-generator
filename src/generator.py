#!/usr/bin/env python

import sys
from src.expression import split
from src.evaluation import evaluate, execute
from src.builtin import to_s

def generator(fin, fout):
    scope = {
        'to_s': to_s
    }
    exec_code = []
    base_indent = [-1]

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
            sys.stdout.write("\n")
            continue

        sp_exprs = split(s)
        result = evaluate(sp_exprs, scope)

        fout.write("".join(map(to_s, result)))
        fout.write("\n")
    if len(exec_code) > 0:
        execute(exec_code, scope, fout)

