#!/usr/bin/env python

def split(s):
    result = []; el = ""
    eval_mode = 0
    level = 0; prev_escape = 0; in_string = None
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
            if eval_mode in [1, 8, 16, 32]:
                if c in '\'"':
                    if in_string is None:
                        in_string = c
                    elif not prev_escape and in_string == c:
                        in_string = None
            if eval_mode == 1 and not in_string:
                if c == '`': level = 0
            if eval_mode == 2 and not prev_escape:
                if c == '"': level = 0
            if eval_mode == 4 and not prev_escape:
                if c == "'": level = 0
            if eval_mode == 8 and not in_string:
                if c == '[': level += 1
                if c == ']': level -= 1
            if eval_mode == 16 and not in_string:
                if c == '(': level += 1
                if c == ')': level -= 1
            if eval_mode == 32 and not in_string:
                if c == '{': level += 1
                if c == '}': level -= 1

            if level == 0: eval_mode = 0
        if c in ' \t' and eval_mode == 0:
            if len(el) > 0:
                result.append(el); el = ""
            result.append(c)
        elif eval_mode not in [0, 1] or c != '`' or in_string:
            el += c
        prev_escape = (c == '\\')
    if len(el) > 0:
        result.append(el)
    while len(result) > 0 and result[-1] == " ":
        result.pop()
    return result

