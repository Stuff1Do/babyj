from tokens import Token, TokenType
from tokentype import *


class ParserJ:
    def __init__(self, tok):
        self.tok = tok  
        self.current = 0

    def peek(self):
        if self.current < len(self.tok):
            return self.tok[self.current]
        return Token(TokenType.EOF, '', -1,-1)
    
    def _advance(self):
        self.current += 1

    def parse(self):
        return self.expression()
    
    def expression(self):
        nodeE = self.term()
        while self.peek() in (TokenType.ADDITION, TokenType.SUBTRACT):
            op = self.peek()
            self._advance()
            nodeE2 = self.term()
            nodeE = (op.value, op.type, nodeE, nodeE2)
        return nodeE
    

    def term(self):
        nodeT = self.factor()
        while self.peek() in (TokenType.MULTIPLY, TokenType.DIVIDE,TokenType.EXPONENTIATION, TokenType.FLOORDIVISION, TokenType.MODULUS):
            op = self.peek()
            self._advance
            nodeT2 = self.factor()
            nodeT = (op.value, op.type, nodeT, nodeT2)
        return nodeT
    
    def factor(self):
        tok = self.peek()
        if tok == TokenType.NUMBER:
            self._advance()
            return ('number', tok.value)
        raise SyntaxError(f'Unexpected token {tok.type}', tok.line)

