Python Text Generator
====

Pythonを使ってテキストを生成できるツールです。
競技プログラミングにおいて、CLI上で入力を簡単に生成するのを想定してます。

erubyのようにループ展開で文字列を生成する機能は現在ついておりません。

## Requirement

Python 2.7 or Python 3.5 を想定しています。

## Install

```sh
$ git clone https://github.com/tjkendev/python-text-generator
$ cd python-text-generator
$ python setup.py install
```

## Usage

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

