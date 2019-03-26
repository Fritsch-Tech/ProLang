from Token import Token
from Constants import Token_type

def lex(content: list):
    tokens = []
    tokens = []
    for line_index,line in enumerate(content):
        tokens_line = []
        token = ''
        string_open = False
        for c in line:
            if c == '"' or c == "'":
                if string_open:
                    string_open = False
                    tokens_line.append(Token(Token_type.STRING,token))
                    token = ''
                else:
                    string_open = True
            elif c == '(':
                __add_previous(token,tokens_line)
                token = ''
                tokens_line.append(Token(Token_type.PAR_OPEN,None))
            elif c == ')':
                __add_previous(token,tokens_line)
                token = ''
                tokens_line.append(Token(Token_type.PAR_CLOSE,None))
            elif c == '.':
                __add_previous(token,tokens_line)
                token = ''
                tokens_line.append(Token(Token_type.PARENT,None))
            elif c == '+':
                __add_previous(token,tokens_line)
                token = ''
                tokens_line.append(Token(Token_type.ADD,None))
            elif c == '-':
                __add_previous(token,tokens_line)
                token = ''
                tokens_line.append(Token(Token_type.SUB,None))
            elif c == '*':
                __add_previous(token,tokens_line)
                token = ''
                tokens_line.append(Token(Token_type.MUL,None))
            elif c == '/':
                __add_previous(token,tokens_line)
                token = ''
                tokens_line.append(Token(Token_type.DIV,None))
            elif c == '=':
                __add_previous(token,tokens_line)
                token = ''
                if tokens_line[-1].token_type == Token_type.ASSIGN:
                    tokens_line[-1] = Token(Token_type.COMPARE,None)
                else:
                    tokens_line.append(Token(Token_type.ASSIGN,None))
            elif c == ' ':
                __add_previous(token,tokens_line)
                token = ''
            else:
                token += c

        if string_open:
            raise Exception('Open string in Line {line}'.format(line=line_index))
        if token != '':
            __add_previous(token,tokens_line)
            token = ''
        if tokens_line != []:
            tokens.append(tokens_line)
    tokens.append([Token(Token_type.EOF,None)])
    print('TOKENS:')
    for line in tokens:
        print(line)
    print('')
    print('='*100)
    print('')
    return(tokens)

def __add_previous(token: str,tokens_line: list):
    token.replace(' ','')
    if token.isdigit():
        tokens_line.append(Token(Token_type.INTEGER,int(token)))
    elif token != '':
        if token == 'ADD':
            tokens_line.append(Token(Token_type.ADD,None))
        elif token == 'SUB':
            tokens_line.append(Token(Token_type.SUB,None))
        elif token == 'MUL':
            tokens_line.append(Token(Token_type.MUL,None))
        elif token == 'DIV':
            tokens_line.append(Token(Token_type.DIV,None))
        elif token == 'IS':
            tokens_line.append(Token(Token_type.ASSIGN,None))
        elif token == 'SUB':
            tokens_line.append(Token(Token_type.SUB,None))
        else:
            tokens_line.append(Token(Token_type.COMMAND,token))
    token = ''
