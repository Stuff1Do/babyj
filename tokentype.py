from enum import Enum

class TokenType(Enum):

    PLUS = '+'
    MINUS = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    ASSIGN = '='
    SEMICOLON = ';' 
    QUOTES = '"'
    LPAREN = '('
    RPAREN = ')'

    EQUALS = '=='
    NEQ = '!='
    LTEQ = '<='
    GTEQ = '>='
    LT = '<'
    GT = '>'


    PRINT  = 'print'
    LET = 'LET'
    NAME = 'NAME'
    NUMBER = 'NUMBER'

    operators = {'+': PLUS, '-': MINUS, '*': MULTIPLY, '/':DIVIDE}