from tokens import Token, TokenType

class Lexer:
    def __init__(self, src):
         self.src = src
         self.ln = 1
         self.col = 0
         self.current_char = self.src[0] if self.src else None
         self.pos = 0
         self._advance()
    def _advance(self):
        if self.pos < len(self.src):
              self.current_char = self.src[self.pos]
              self.pos += 1
              self.col += 1
        else:
             self.current_char = None
    def consume_while(self, test):
        result = ''
        start_col = self.col
        while self.current_char is not None and test(self.current_char):
            result += self.current_char
            self._advance()
        return result, start_col
    def tokenize(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char.isspace():
                if self.current_char == '\n':
                    self.ln += 1
                    self.col = 0
                self._advance()
            elif self.current_char.isalpha():
                text, start_col = self.consume_while(lambda c: c.isalnum())
                if text == 'let':
                    tokens.append(Token(TokenType.LET, text, self.ln,start_col))
                elif text == 'print':
                    tokens.append(Token(TokenType.PRINT, text, self.ln, start_col))
                else:
                    tokens.append(Token(TokenType.NAME, text, self.ln, start_col))
            elif self.current_char.isdigit():
                text, start_col = self.consume_while(lambda c: c.isdigit())
                tokens.append(Token(TokenType.NUMBER, int(text), self.ln, start_col))
            elif self.current_char in TokenType.operators:
                token_type = TokenType.operators[self.current_char]
                tokens.append(Token(token_type, self.current_char, self.ln, self.col))
                self._advance()        
        return tokens
    
def run(src):
    lexer = Lexer(src)
    tokens = lexer.tokenize()
    return tokens
             