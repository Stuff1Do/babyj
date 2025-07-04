from tokens import Token, TokenType    
from lexer import IllegalSyntaxError, Lexer
from tokentype import *
from asttype import ASTType

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

    def _previous(self):
        return self.tok[self.current - 1]
                  
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
    def _toktype_to_asttype(self, token_type):
        return {
            TokenType.STRING: ASTType.STRING,
            TokenType.INTEGER: ASTType.INTEGER,
            TokenType.FLOAT: ASTType.FLOAT,
            TokenType.IDENTIFIER: ASTType.IDENTIFIER
        }[token_type]

    def parse(self):
        statements = []
        while self._peek().type != TokenType.EOF:
            stmt = self.statement()
            statements.append(stmt)
        return statements
    def print_statement(self):
        self._expect(TokenType.LPAREN)
        
        expr = None
        tok = self._peek()
        if self._peek().type in (TokenType.STRING, TokenType.INTEGER, TokenType.FLOAT, TokenType.IDENTIFIER):
            self._advance()
            if tok.type == TokenType.STRING:
                expr = (ASTType.STRING, tok.value)
            elif tok.type == TokenType.INTEGER:
                expr = (ASTType.INTEGER, tok.value)
            elif tok.type == TokenType.FLOAT:
                expr = (ASTType.FLOAT, tok.value)
            elif tok.type == TokenType.IDENTIFIER:
                expr = (ASTType.IDENTIFIER, tok.value)
        else:
            raise IllegalSyntaxError(f"Invalid print content: {self._peek().type}", self._peek().line)
        
        self._expect(TokenType.RPAREN)
        return (ASTType.PRINT, expr)
    def return_statement(self):
        
        expr = None
        tok = self._peek()
        if self._peek().type in (TokenType.STRING, TokenType.INTEGER, TokenType.FLOAT, TokenType.IDENTIFIER):
            self._advance()
            if tok.type == TokenType.STRING:
                expr = (ASTType.STRING, tok.value)
            elif tok.type == TokenType.INTEGER:
                expr = (ASTType.INTEGER, tok.value)
            elif tok.type == TokenType.FLOAT:
                expr = (ASTType.FLOAT, tok.value)
            elif tok.type == TokenType.IDENTIFIER:
                expr = (ASTType.IDENTIFIER, tok.value)
        else:
            raise IllegalSyntaxError(f"Invalid return type, got {self._peek().type}", self._peek().line)
        return (ASTType.RETURN, expr)
    def condition(self):
        lhs_tok = self._peek()
        
        if lhs_tok.type not in (TokenType.STRING, TokenType.INTEGER, TokenType.FLOAT, TokenType.IDENTIFIER):
            raise IllegalSyntaxError(f"Illegal condition operand, got {lhs_tok.type}", lhs_tok.line)
        
        self._advance()
        lhs = (self._toktype_to_asttype(lhs_tok.type), lhs_tok.value)

        
        op = self._matches(*EQUAL_OPS.values(), TokenType.EQUALS, TokenType.LT, TokenType.GT)
        if not op:
            raise IllegalSyntaxError("Expected comparison operator in condition", self._peek().line)

        
        rhs_tok = self._matches(TokenType.STRING, TokenType.INTEGER, TokenType.FLOAT, TokenType.IDENTIFIER)
        if not rhs_tok:
            raise IllegalSyntaxError("Expected right-hand side operand in condition", self._peek().line)
        
        rhs = (self._toktype_to_asttype(rhs_tok.type), rhs_tok.value)

        return (ASTType.BINARY_COND, lhs, op, rhs)

    def if_block(self):
        condition = self.condition()
        self._expect(TokenType.THEN)
        self._expect(TokenType.LBRACES)
        block = []
        while self._peek().type != TokenType.RBRACES:
            if self._peek().type == TokenType.EOF:
                raise IllegalSyntaxError("Missing '}' at the end of if-else block", self._peek().line)
            block.append(self.statement())
        self._expect(TokenType.RBRACES)
        return (ASTType.IF, condition, block)
    def statement(self):
        if self._matches(TokenType.LET):
            return self.declaration()
        elif self._is_reassignment():
            return self.reassignment()
        elif self._matches(TokenType.PRINT):
            return self.print_statement()
        elif self._matches(TokenType.RETURN):
            return self.return_statement()
        elif self._matches(TokenType.IF):
            return self.if_block()
        else:
            return self.expression()    
    def reassignment(self):
        name = self._expect(TokenType.IDENTIFIER)
        self._expect(TokenType.ASSIGN)
        value = self.expression()
        return (ASTType.VAR_ASSIGN, name.value, value)
    
    def declaration(self):
        name = self._expect(TokenType.IDENTIFIER)
        if self._matches(TokenType.ASSIGN):
            value = self.expression()
            return (ASTType.VAR_DECL, name.value, value)
        return (ASTType.VAR_DECL, name.value)
    
    def expression(self):
        nodeE = self.term()
        while self._peek().type in (TokenType.ADDITION, TokenType.SUBTRACT):
            op = self._peek()
            self._advance()
            nodeE2 = self.term()
            nodeE = (ASTType.BINOPS, op.type, nodeE, nodeE2)
        return nodeE
    
    def term(self):
        nodeT = self.factor()
        while self._peek().type in (TokenType.MULTIPLY, TokenType.DIVIDE,TokenType.EXPONENTIATION, TokenType.FLOORDIVISION, TokenType.MODULUS):
            op = self._peek()   
            self._advance()
            nodeT2 = self.factor()
            nodeT = (ASTType.BINOPS, op.type, nodeT, nodeT2)
        return nodeT
    
    def factor(self):
        tok = self._peek()
        if tok.type == TokenType.SUBTRACT:
            op = self._peek()
            self._advance()
            operand  = self.factor()    
            return (ASTType.UNARYOPS, op.type, operand)
        if tok.type == TokenType.INTEGER:
            self._advance()
            return (ASTType.INTEGER, tok.value)
        if tok.type == TokenType.FLOAT:
            self._advance()
            return(ASTType.FLOAT, tok.value)
        if tok.type == TokenType.STRING:
            self._advance()
            return(ASTType.STRING, tok.value)
        if tok.type == TokenType.IDENTIFIER:
            self._advance()
            return (ASTType.IDENTIFIER, tok.value)
        if tok.type == TokenType.LPAREN:
            self._advance()
            node = self.expression()
            self._expect(TokenType.RPAREN)
            return node
        

        raise IllegalSyntaxError(f'Unexpected token {tok.type}', tok.line)


