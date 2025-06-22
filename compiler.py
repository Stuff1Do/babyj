class My:
    def __init__(self, code):
        self.code = code
        self.line_nr = 0

    def raise_error(self, message):
        raise ValueError(f'{self.line_nr}: {message}')

    def tokens(self):
        for line in self.code.strip().split('\n'):
            self.line_nr += 1
            for token in line.strip().split(' '):
                if token == 'print':
                    yield (token,)
                elif token.isnumeric():
                    yield ('number', int(token))
                else:
                    self.raise_error(f'Syntax Error: Invalid token {token}')
            yield ('\n',)