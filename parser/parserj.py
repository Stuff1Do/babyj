from tokens import Token, TokenType
from lexer import *
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

    def matches(self, *types):
        if self.peek().type in types:
            tok = self.peek()
            self.current += 1
            return tok
        return None


    def expect(self, token_type):
        tok = self.matches(token_type)
        if tok:
            return tok
        raise SyntaxError(f"Expected {token_type}, got {self.peek().type}", self.peek().line)

    def parse(self):
        return self.expression()
    
    def expression(self):
        nodeE = self.term()
        while self.peek().type in (TokenType.ADDITION, TokenType.SUBTRACT):
            op = self.peek()
            self._advance()
            nodeE2 = self.term()
            nodeE = ("BINOPS", op.type, nodeE, nodeE2)
        return nodeE
    
    def term(self):
        nodeT = self.factor()
        while self.peek().type in (TokenType.MULTIPLY, TokenType.DIVIDE,TokenType.EXPONENTIATION, TokenType.FLOORDIVISION, TokenType.MODULUS):
            op = self.peek()
            self._advance()
            nodeT2 = self.factor()
            nodeT = ("BINOPS", op.type, nodeT, nodeT2)
        return nodeT
    
    def factor(self):
        tok = self.peek()
        if tok.type == TokenType.SUBTRACT:
            op = self.peek()
            self._advance()
            operand  = self.factor()    
            return ('UNARYOPS', op.type, operand)
        if tok.type == TokenType.INTEGER:
            self._advance()
            return ('INTEGER', tok.value)
        if tok.type == TokenType.FLOAT:
            self._advance()
            return('FLOAT', tok.value)
        if tok.type == TokenType.STRING:
            self._advance()
            return('STRING', tok.value)
        if tok.type == TokenType.LPAREN:
            self._advance()
            node = self.expression()
            self.expect(TokenType.RPAREN)
            return node
        

        raise IllegalSyntaxError(f'Unexpected token {tok.type}', tok.line)


