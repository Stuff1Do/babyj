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
    PRINT = 'PRINT'
    RETURN = 'RETURN'
    IF = 'IF'
    BINARY_COND = 'BINARY_COND'
    def __str__(self):
        return f"ASTType.{self.name}"

    def __repr__(self):
        return str(self)