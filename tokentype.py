from enum import Enum

class TokenType(Enum):

    #Single Operators
    PLUS = '+'
    SUBTRACT = '-'
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
    LBRACES = '{'
    RBRACES = '}'
    LBRACKET = '['
    RBRACKET = ']'

    #Special Cases
    ASSIGN = '='
    EQUALS = '=='
    NEQ = '!='
    LTEQ = '<='
    GTEQ = '>='
    PLUSEQ = '+='
    SUBEQ = '-='
    MULTEQ = '*='
    DIVEQ = '/='
    
    #TYPES
    NAME = 'NAME'
    NUMBER = 'NUMBER'
    STRING = 'STRING'

    #KEYWORDS
    PRINT  = 'print'
    LET = 'LET'
    IF = 'IF'
    THEN = 'THEN'
    REPEAT = 'REPEAT'
    UNTIL = 'UNTIL'
    ELSEIF = 'ELSEIF'
    ELSE = 'ELSE'
    WHILE = 'WHILE'
    DO = 'DO'
    FOREACH= 'FOREACH'

OPERATORS = {'+': TokenType.PLUS, 
             '-': TokenType.SUBTRACT, 
             '*': TokenType.MULTIPLY, 
             '/': TokenType.DIVIDE,
             '<': TokenType.LT,
             '>': TokenType.GT,
             '!': TokenType.NOT}
EQUAL_OPS = {'!=': TokenType.NEQ,
            '<=':TokenType.NEQ,
            '>=':TokenType.GTEQ,
            '+=': TokenType.PLUSEQ,
            '-=': TokenType.SUBEQ,
            '*=': TokenType.MULTEQ,
            '/=': TokenType.DIVEQ}
PARENS = {'(': TokenType.LPAREN,
          ')': TokenType.RPAREN,
          '{':TokenType.LBRACES,
          '}': TokenType.RBRACES,
          '[': TokenType.LBRACKET,
          ']':TokenType.RBRACKET,}
KEYWORDS = {'let': TokenType.LET,
            'print': TokenType.PRINT,
            'if':TokenType.IF,
            'then': TokenType.THEN,
            'repeat': TokenType.REPEAT,
            'until': TokenType.UNTIL,
            'elseif': TokenType.ELSEIF,
            'else': TokenType.ELSE,
            'while': TokenType.WHILE,
            'do': TokenType.DO,
            'foreach': TokenType.FOREACH}

