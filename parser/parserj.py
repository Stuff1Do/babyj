from tokens import Token, TokenType    
from lexer import *
from tokentype import *

class ParserJ:
    def __init__(self, tok):
        self.tok = tok  
        self.current = 0

    def _peek(self, n=0):
        if self.current + n < len(self.tok):
            return self.tok[self.current + n]
        return Token(TokenType.EOF, '', -1,-1)
    
    def _advance(self):
        self.current += 1   

    def _matches(self, *types):
        if self._peek().type in types:
            tok = self._peek()
            self._advance()
            return tok
        return None


    def _expect(self, token_type):
        tok = self._matches(token_type)
        if tok:
            return tok
        raise IllegalSyntaxError(f"Expected {token_type}, got {self._peek().type}", self._peek().line)
    def _is_reassignment(self):
        return (self._peek().type == TokenType.IDENTIFIER and 
                self._peek(1).type == TokenType.ASSIGN)
    
    def parse(self):
        statements = []
        while self._peek().type != TokenType.EOF:
            stmt = self.statement()
            statements.append(stmt)
        return statements
    
    def statement(self):
        if self._matches(TokenType.LET):
            return self.declaration()
        elif self._is_reassignment():
            return self.reassignment()
        else:
            return self.expression()    
    def reassignment(self):
        name = self._expect(TokenType.IDENTIFIER)
        self._expect(TokenType.ASSIGN)
        value = self.expression()
        return ('VAR_ASSIGN', name.value, value)
    
    def declaration(self):
        name = self._expect(TokenType.IDENTIFIER)
        if self._matches(TokenType.ASSIGN):
            value = self.expression()
            return ('VAR_DECL', name.value, value)
        return ('VAR_DECL', name.value)
    
    def expression(self):
        nodeE = self.term()
        while self._peek().type in (TokenType.ADDITION, TokenType.SUBTRACT):
            op = self._peek()
            self._advance()
            nodeE2 = self.term()
            nodeE = ("BINOPS", op.type, nodeE, nodeE2)
        return nodeE
    
    def term(self):
        nodeT = self.factor()
        while self._peek().type in (TokenType.MULTIPLY, TokenType.DIVIDE,TokenType.EXPONENTIATION, TokenType.FLOORDIVISION, TokenType.MODULUS):
            op = self._peek()
            self._advance()
            nodeT2 = self.factor()
            nodeT = ("BINOPS", op.type, nodeT, nodeT2)
        return nodeT
    
    def factor(self):
        tok = self._peek()
        if tok.type == TokenType.SUBTRACT:
            op = self._peek()
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
        if tok.type == TokenType.IDENTIFIER:
            self._advance()
            return ('IDENTIFIER', tok.value)
        if tok.type == TokenType.LPAREN:
            self._advance()
            node = self.expression()
            self._expect(TokenType.RPAREN)
            return node
        

        raise IllegalSyntaxError(f'Unexpected token {tok.type}', tok.line)


