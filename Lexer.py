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
            if c == '"':
                if string_open:
                    string_open = False
                    tokens_line.append(Token(Token_type.STRING,token))
                    token = ''
                else:
                    string_open = True
            elif c == '(':
                __add_previous(token,tokens_line)
                token = ''
                tokens_line.append(Token(Token_type.PAR_OPEN,c))
            elif c == ')':
                __add_previous(token,tokens_line)
                token = ''
                tokens_line.append(Token(Token_type.PAR_CLOSE,c))
            elif c == '+':
                __add_previous(token,tokens_line)
                token = ''
                tokens_line.append(Token(Token_type.ADD,c))
            elif c == '-':
                __add_previous(token,tokens_line)
                token = ''
                tokens_line.append(Token(Token_type.SUB,c))
            elif c == '*':
                __add_previous(token,tokens_line)
                token = ''
                tokens_line.append(Token(Token_type.MUL,c))
            elif c == '/':
                __add_previous(token,tokens_line)
                token = ''
                tokens_line.append(Token(Token_type.DIV,c))
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
    if token.isdigit():
        tokens_line.append(Token(Token_type.INTEGER,token))
    else:
        tokens_line.append(Token(Token_type.COMMAND,token))
    token = ''
