#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import Lexer
import Interpreter

def main(filename: str):
    content = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            content.append(line.replace('\n',''))

    print('RAW:')
    print(content)
    print('')
    print('='*100)
    print('')

    Interpreter.interpret(Lexer.lex(content))

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except Exception as e:
        print('Enter filename')
    main(filename)
