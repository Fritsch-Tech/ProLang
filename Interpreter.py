#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import Lexer

def interpret(filename: str):
    contetnt = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            contetnt.append(line.replace('\n',''))
    Lexer.lex(contetnt)

if __name__ == "__main__":
    try:
        interpret(sys.argv[1])
    except Exception as e:
        print(e)
