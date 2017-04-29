Python Text Generator
====

Python Text Generator is text generator using Python expressions and statements.

This tool allows you to generate texts by writing Python expressions directly.

## Install

```sh
$ git clone https://github.com/tjkendev/python-text-generator
$ cd python-text-generator
$ python setup.py install
```

## Usage

You can generate text from stdin by calling `python-text-generator` with no parameters,
and output generated text as stdout.
```sh
$ echo "[i**2 for i in range(9)]" | python-text-generator
0 1 4 9 16 25 36 49 64
```

To generate text from a file, you can specify file path with `-i` parameters.

For example, to generate texts from the file below:
```sh
$ cat test
1 2 3 "a" ["b", "c"]
[1,2,3] [1,2,3] # comment
10*"a"
`"b" * 15` `1 + 2 * 3`
10**9+7

% # use Python statement and variable
% x = [1, 2]; y = [9, 3, 4, "d"]
x[0] x y*2
{4, 5, 6}

% # import and use library
% import random
% A=[random.randint(1, 10) for i in range(3)]
A

% # to_s function
% B=[[1,2,3],[4,5],[6,[7,8]]]
to_s(A, "\n")
to_s(B, ["\n","-"])
```

You can specify the file like below:
```sh
$ python-text-generator -i test
1 2 3 a b c
1 2 3 1 2 3
aaaaaaaaaa
bbbbbbbbbbbbbbb 7
1000000007

1 1 2 9 3 4 d 9 3 4 d
4 5 6

2 7 6

2
7
6
1-2-3
4-5
6-7 8
```

Also, you can specify file path to write generated text with `-o` parameters.
