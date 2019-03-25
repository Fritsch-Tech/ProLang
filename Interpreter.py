from Token import Token
from Constants import Token_type

def interpret(tokens: list):
    for line_index,token_line in enumerate(tokens):
        for index,token in enumerate(token_line):
            try:
                if token.token_type == Token_type.ADD:
                    token_line[index] = Token(Token_type.INTEGER,token_line[index-1].value+token_line[index+1].value)
                elif token.token_type == Token_type.SUB:
                    token_line[index] = Token(Token_type.INTEGER,token_line[index-1].value-token_line[index+1].value)
                elif token.token_type == Token_type.MUL:
                    token_line[index] = Token(Token_type.INTEGER,token_line[index-1].value*token_line[index+1].value)
                elif token.token_type == Token_type.DIV:
                    token_line[index] = Token(Token_type.INTEGER,token_line[index-1].value/token_line[index+1].value)
                else:
                    continue
                token_line.pop(index+1)
                token_line.pop(index-1)
            except:
                raise Exception('Error in Line {line} near {token_value}'.
                    format(line=line_index,token_value=token.value))


    print('TOKENS:')
    for line in tokens:
        print(line)
    print('')
    print('='*100)
    print('')
