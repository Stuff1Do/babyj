from sys import argv
from lexer import *
from parserj import *
from pprint import pprint
def read(file):
    contents = open(file, 'r').read()
    tokens, error = run(contents)
    return tokens, error

if __name__ == '__main__':
    tokens, error = read(argv[1])
    if error:
        print(error.as_string())
    else:
        ast = ParserJ(tokens).parse()
        pprint(ast)
    