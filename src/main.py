#!/usr/bin/env python
import src.expression as expression
import sys, argparse
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
    if isinstance(val, collections.Iterable) and not isinstance(val, str):
        return c_delimiter.join(map(lambda x: to_s(x, n_delimiter), val))
    return str(val)

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
            old_stdout, sys.stdout = sys.stdout, fout
            exec("\n".join(exec_code), scope)
            sys.stdout = old_stdout
            del exec_code[:]
        if len(s) == 0:
            sys.stdout.write("\n")
            continue

        sp_exprs = expression.split(s)
        result = expression.evaluate(sp_exprs, scope)

        fout.write("".join(map(to_s, result)))
        fout.write("\n")
    if len(exec_code) > 0:
        old_stdout, sys.stdout = sys.stdout, fout
        exec("\n".join(exec_code), scope)
        sys.stdout = old_stdout

def entry():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest="input_file", metavar="<file>", help="Read input from <file>")
    parser.add_argument('-o', dest="output_file", metavar="<file>", help="Write output to <file>")
    args = parser.parse_args()
    if args.input_file:
        fin = open(args.input_file, 'r')
    else:
        fin = sys.stdin
    if args.output_file:
        fout = open(args.output_file, 'w')
    else:
        fout = sys.stdout
    generator(fin, fout)
    fin.close()
    fout.close()

if __name__ == "__main__":
    entry()
