from Token import Token
from Constants import Token_type

def lex(content: list):
    print(content)
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
                tokens_line.append(Token(Token_type.COMMAND,token))
                token = ''
                tokens_line.append(Token(Token_type.PAR_OPEN,c))
            elif c == ')':
                tokens_line.append(Token(Token_type.COMMAND,token))
                token = ''
                tokens_line.append(Token(Token_type.PAR_CLOSE,c))

            else:
                token += c

        if string_open:
            raise Exception('Open string in Line {line}'.format(line=line_index))
        if tokens_line != []:
            tokens.append(tokens_line)
    tokens.append([Token(Token_type.EOF,None)])
    for line in tokens:
        print(line)
    return(tokens)
