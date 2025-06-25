from enum import Enum

class TokenType(Enum):

    #Single Operators
    PLUS = '+'
    MINUS = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    LT = '<'
    GT = '>'

    #CHARACTERS
    SEMICOLON = ';' 
    QUOTES = '"'
    LPAREN = '('
    RPAREN = ')'

    #Special Cases
    ASSIGN = '='
    EQUALS = '=='
    NEQ = '!='
    LTEQ = '<='
    GTEQ = '>='
    


    PRINT  = 'print'
    LET = 'LET'
    NAME = 'NAME'
    NUMBER = 'NUMBER'

OPERATORS = {'+': TokenType.PLUS, 
             '-': TokenType.MINUS, 
             '*': TokenType.MULTIPLY, 
             '/': TokenType.DIVIDE,
             '<': TokenType.LT,
             '>': TokenType.GT}
