from enum import Enum

class ASTType(Enum):
    BINOPS = 'BINOPS'
    UNARYOPS = 'UNARYOPS'
    VAR_DECL = 'VAR_DECL'
    VAR_ASSIGN = 'VAR_ASSIGN'
    INTEGER = 'INTEGER'
    STRING = 'STRING'
    FLOAT = 'FLOAT'
    IDENTIFIER = 'IDENTIFIER'
    
        