#!/usr/bin/env python
import sys, argparse

def next_deli(lst):
    if len(lst) <= 1:
        return [' ']
    return lst[1:]

def split_expr(s):
    sps = []
    el = ""
    eval_mode = 0
    level = 0
    for c in s:
        if eval_mode == 0:
            if c == '#': break
            if c == '`': eval_mode = 1
            if c == '"': eval_mode = 2
            if c == "'": eval_mode = 4
            if c == '[': eval_mode = 8
            if c == '(': eval_mode = 16
            if c == '{': eval_mode = 32

            if eval_mode != 0: level = 1
        else:
            if eval_mode == 1:
                if c == '`': level = 0
            if eval_mode == 2:
                if c == '"': level = 0
            if eval_mode == 4:
                if c == "'": level = 0
            if eval_mode == 8:
                if c == '[': level += 1
                if c == ']': level -= 1
            if eval_mode == 16:
                if c == '(': level += 1
                if c == ')': level -= 1
            if eval_mode == 32:
                if c == '{': level += 1
                if c == '}': level -= 1

            if level == 0: eval_mode = 0
        if c in ' \t' and eval_mode == 0:
            if len(el) > 0:
                sps.append(el); el = ""
            sps.append(c)
        elif eval_mode not in [0, 1] or c != '`':
            el += c
    if len(el) > 0:
        sps.append(el)
    return sps

def evaluate_expr(s_lst, scope):
    result = []
    for el in s_lst:
        if el == " ":
            val = el
        else:
            val = eval(el, scope)
        if val is not None:
            result.append(val)
    return result

def to_s(val, delimiter=None):
    delimiter = delimiter or ' '
    if type(delimiter) == str:
        delimiter = [delimiter]
    c_delimiter = delimiter[0]
    result = []
    if type(val) in [list, tuple, set]:
        return c_delimiter.join(map(lambda x: to_s(x, next_deli(delimiter)), val))
    elif type(val) == dict:
        return c_delimiter.join(map(lambda x: to_s(x, next_deli(delimiter)), val.keys()))
    return str(val)

def main(fin, fout):
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
            exec("\n".join(exec_code), scope)
            del exec_code[:]
        if len(s) == 0:
            sys.stdout.write("\n")
            continue

        sp_exprs = split_expr(s)
        result = evaluate_expr(sp_exprs, scope)

        fout.write("".join(map(to_s, result)))
        fout.write("\n")

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
    main(fin, fout)
    fin.close()
    fout.close()

if __name__ == "__main__":
    entry()
