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

    LET = 'LET'
    IDENTIFIER = 'IDENTIFIER'
    NUMBER = 'NUMBER'