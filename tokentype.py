from enum import Enum

class TokenType(Enum):

    #Single Operators
    ADDITION = '+'
    SUBTRACT = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    MODULUS ='%'
    LT = '<'
    GT = '>'
    NOT = '!'

    #Double Operators
    INCREMENT = '++'
    DECREMENT = '--'
    EXPONENTIATION = '**'
    FLOORDIVISION = '//'

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
    RETURN  = 'return'
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

    EOF = 'EOF'

OPERATORS = {'+': TokenType.ADDITION, 
             '-': TokenType.SUBTRACT, 
             '*': TokenType.MULTIPLY, 
             '/': TokenType.DIVIDE,
             '<': TokenType.LT,
             '>': TokenType.GT,
             '!': TokenType.NOT,
             '%': TokenType.MODULUS}
DOUBLE_OPERATORS = {'++': TokenType.INCREMENT,
                    '--': TokenType.DECREMENT,
                    '**': TokenType.EXPONENTIATION,
                    '//': TokenType.FLOORDIVISION}
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
            'return': TokenType.RETURN,
            'if':TokenType.IF,
            'then': TokenType.THEN,
            'repeat': TokenType.REPEAT,
            'until': TokenType.UNTIL,
            'elseif': TokenType.ELSEIF,
            'else': TokenType.ELSE,
            'while': TokenType.WHILE,
            'do': TokenType.DO,
            'foreach': TokenType.FOREACH}

