#!/usr/bin/env python
import sys, argparse
from src.generator import generator

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
