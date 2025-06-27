from sys import argv
from lexer import *
from parserj import *

def parse(file):
    contents = open(file, 'r').read()
    tokens, error = run(contents)
    return tokens, error

if __name__ == '__main__':
    tokens, error = parse(argv[1])
    if error:
        print(error.as_string())
    else:
        for token in tokens:
            print(token)
