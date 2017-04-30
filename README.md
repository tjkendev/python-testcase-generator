Python Text Generator
====

Python Text Generator is text generator using Python expressions and statements.

This tool allows you to generate text by writing Python expressions directly.

## Install

Installation using `setup.py`.
```sh
$ git clone https://github.com/tjkendev/python-text-generator
$ cd python-text-generator
$ python setup.py install
```
Installation using pip.
```sh
$ git clone https://github.com/tjkendev/python-text-generator
$ cd python-text-generator
$ pip install python-text-generator
```

## Usage

By calling `python-text-generator` with no parameters, text is generated from stdin
and outputted as stdout.
```sh
$ echo "[i**2 for i in range(9)]" | python-text-generator
0 1 4 9 16 25 36 49 64
```

To generate text from a file, you can specify input file path with `-i` parameter.  
For example, to generate text from the file below:
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
$ python-text-generator -i test.txt
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

Also, to write generated text to a file, specify output file path with `-o` parameter.
```sh
$ python-text-generator -i test.txt -o output.txt
```
