from tokentype import TokenType 

class Token:
    def __init__(self, type: TokenType, value, line: int, column: int):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        if self.value is not None:
            return f'{self.type.name}: {self.value} (line {self.line}, col {self.column})'
        return f'{self.type.name} (line {self.line}, col {self.column})'
