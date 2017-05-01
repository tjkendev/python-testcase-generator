Python Test Case Generator
====

Python Test Case Generator is a test case generator using Python expressions and statements.

This tool allows you to generate a test case by writing Python expressions directly.

## Install

Installation using `setup.py`.
```sh
$ git clone https://github.com/tjkendev/python-testcase-generator
$ cd python-testcase-generator
$ python setup.py install
```
Installation using pip.
```sh
$ pip install python-testcase-generator
```

## Usage

By calling `python-testcase-generator` (or `pytcgen`) with no parameters, a test case is generated from stdin
and outputted as stdout.
```sh
$ echo "[i**2 for i in range(9)]" | python-testcase-generator
0 1 4 9 16 25 36 49 64
```

To generate a test case from a file, you can specify input file path with `-i` parameter.  
For example, to generate a test case from the file below:
```sh
$ cat test.txt
1 2 3 "a" ["b", "c"]
[1,2,3] [1,2,3] # comment
10*"a"
% # You can write expressions including space by using backquote (`).
% # It does not mean repr() in Python 2. (special specification in this tool)
`"b" * 15` `1 + 2 * 3`
10**9+7

% # use Python statement and variable
% x = [1, 2]; y = [9, 3, 4, "d"]
x[0] x y*2
{4, x[2], 6}

% # import and use library
% import random
% A=[random.randint(1, 10) for i in range(3)]
A

% # to_s function
% B=[[1,2,3],[4,5],[6,[7,8]]]
to_s(A, "\n")
to_s(B, ["\n","-"])
```

You can specify input file path as follows:
```sh
$ python-testcase-generator -i test.txt
1 2 3 a b c
1 2 3 1 2 3
aaaaaaaaaa
bbbbbbbbbbbbbbb 7
1000000007

1 1 2 9 3 4 d 9 3 4 d
2 4 6

10 2 7

10
2
7
1-2-3
4-5
6-7 8
```

Also, to write generated a test case to a file, specify output file path with `-o` parameter.
```sh
$ python-testcase-generator -i test.txt -o output.txt
```
