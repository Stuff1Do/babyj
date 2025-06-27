from lexer import *

def parse(file):
    contents = open(file, 'r').read()
    tokens, error = run(contents)
    return tokens, error