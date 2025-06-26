from enum import Enum

class TokenType(Enum):

    #Single Operators
    PLUS = '+'
    MINUS = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    LT = '<'
    GT = '>'
    NOT = '!'

    #CHARACTERS
    SEMICOLON = ';' 
    QUOTES = '"'
    LPAREN = '('
    RPAREN = ')'
    LBRACKET = '{'
    RBRACKET = '}'

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
    STRING = 'STRING'
OPERATORS = {'+': TokenType.PLUS, 
             '-': TokenType.MINUS, 
             '*': TokenType.MULTIPLY, 
             '/': TokenType.DIVIDE,
             '<': TokenType.LT,
             '>': TokenType.GT,
             '!': TokenType.NOT}
EQUAL_OPS = {'!=': TokenType.NEQ,
            '<=':TokenType.NEQ,
            '>=':TokenType.GTEQ,}