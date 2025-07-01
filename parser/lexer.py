from tokens import Token, TokenType
from tokentype import *
class Error(Exception):
    def __init__(self, name, details, line):
        self.name = name
        self.details = details
        self.line = line
    def as_string(self):
        result = f'{self.name}: {self.details} (at line:{self.line})'
        return result
class IllegalSyntaxError(Error):
    def __init__(self, details, line):
        super().__init__('IllegalSyntaxError', details, line)
class Lexer:
    def __init__(self, src):
         self.src = src
         self.ln = 1         
         self.col = 0
         self.current_char = self.src[0] if self.src else None
         self.pos = 0
         self._advance()
    def peek(self):
        if self.pos < len(self.src):
            result = str(self.src[self.pos])
            return result
        else:
            return None 
        
    def _advance(self): 
        if self.pos < len(self.src):
              self.current_char = self.src[self.pos]
              self.pos += 1
              self.col += 1 
        else:
             self.current_char = None
    def consume_while(self, test, check_dot = False):
        result = ''
        start_col = self.col
        dot_used = False
        while self.current_char is not None:
            if check_dot and self.current_char == '.' and not dot_used:
                if self.peek() and self.peek().isdigit():
                    dot_used = True
                    result += self.current_char
                    self._advance()
                else:
                    raise IllegalSyntaxError(f"Invalid float format", self.ln)
                
            if test(self.current_char):
                result += self.current_char
                self._advance()
            else:
                break
        return result, start_col
    def consume_string(self):
        self._advance()
        result = ''
        col = self.col      
        while self.current_char != '"':
            if self.current_char == None:
                return "not_closed", None
            result += self.current_char
            self._advance()
        return result, col
    def tokenize(self):
        tokens = []
        equals= False
        seenOP = False
        while self.current_char is not None:
            if self.current_char.isspace():
                if self.current_char == '\n':
                    self.ln += 1
                    self.col = 0
                self._advance()
            elif self.current_char.isalpha():
                text, start_col = self.consume_while(lambda c: c.isalnum()) 
                if text in KEYWORDS:
                    token_type = KEYWORDS[text]
                    tokens.append(Token(token_type, text, self.ln, start_col))
                else:
                    tokens.append(Token(TokenType.NAME, text, self.ln, start_col))
            elif self.current_char.isdigit():
                text, start_col = self.consume_while(lambda c: c.isdigit(), check_dot = True)
                if '.' in text:
                    tokens.append(Token(TokenType.FLOAT, float(text), self.ln, start_col))
                else:
                    tokens.append(Token(TokenType.INTEGER, int(text), self.ln, start_col))           
            elif self.current_char in OPERATORS:
                if self.peek()== '=':
                    appe = str(self.current_char + '=')
                    token_type = EQUAL_OPS[appe]
                    tokens.append(Token(token_type, appe, self.ln, self.col))
                    equals = True
                    self._advance()
                elif self.peek() in OPERATORS:
                    doub = self.current_char + self.peek()
                    token_type = DOUBLE_OPERATORS[doub]
                    tokens.append(Token(token_type, doub, self.ln, self.col))
                    seenOP = True
                    self._advance()
                else:  
                    if seenOP == True:
                        seenOP = False
                        self._advance()
                    else:
                        token_type = OPERATORS[self.current_char]
                        tokens.append(Token(token_type, self.current_char, self.ln, self.col))
                        self._advance()      
            elif self.current_char == ';':  
                tokens.append(Token(TokenType.SEMICOLON, self.current_char, self.ln, self.col))
                self._advance()
            elif self.current_char == '=':
                if equals == True:
                    if self.peek() == '=':
                        return [], SyntaxError('"===" not valid', self.ln)
                    equals = False
                    self._advance()
                else:
                    if self.peek() == '=':
                        tokens.append(Token(TokenType.EQUALS, '==', self.ln, self.col))
                        equals = True
                        self._advance()
                    else:
                        tokens.append(Token(TokenType.ASSIGN, self.current_char, self.ln, self.col))
                        self._advance()
                        
            elif self.current_char== '"':
                string, col = self.consume_string()
                if string == 'not_closed':
                    return [], SyntaxError("Quotation not closed!", self.ln)
                tokens.append(Token(TokenType.STRING, f'"{string}"', self.ln, col))
                self._advance()
            elif self.current_char in PARENS:
                token_type = PARENS[self.current_char]
                tokens.append(Token(token_type, self.current_char, self.ln, self.col))
                self._advance()
            else:
                char = self.current_char
                self._advance()
                return [], SyntaxError(f'"{char}"', self.ln)

        return tokens, None
    
def run(src):
    lexer = Lexer(src)
    tokens, error = lexer.tokenize()
    return tokens, error
             