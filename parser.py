class Parser:
    EOF = '\0'

    def __init__(self, input_string):
        self.input = input_string.replace(" ", "") + self.EOF
        self.index = 0
        self.current = self.input[self.index]

    def lookahead(self):
        return self.current

    def next(self):
        self.index += 1
        if self.index < len(self.input):
            self.current = self.input[self.index]
        else:
            self.current = self.EOF
        return self.current

    def match(self, expected_char):
        if self.current == expected_char:
            self.next()
        else:
            self.error(f"Esperado '{expected_char}', encontrado '{self.current}'")

    def error(self, msg):
        raise SyntaxError(f"Erro na coluna {self.index + 1}: {msg}")
    
    def parse(self):
        self.EXPR()
        if self.lookahead() != self.EOF:
            self.error("Entrada não foi completamente consumida")
        return True

    def EXPR(self):
        self.TERM()
        self.EXPR_()

    def EXPR_(self):
        if self.lookahead() == '+':
            self.match('+')
            self.TERM()
            self.EXPR_()
        elif self.lookahead() == '-':
            self.match('-')
            self.TERM()
            self.EXPR_()
        else:
            # ε (vazio) — nada a fazer
            pass

    def TERM(self):
        self.UNARY()
        self.TERM_()

    def TERM_(self):
        if self.lookahead() == '*':
            self.match('*')
            self.UNARY()
            self.TERM_()
        elif self.lookahead() == '/':
            self.match('/')
            self.UNARY()
            self.TERM_()
        else:
            # ε (vazio)
            pass

    def UNARY(self):
        if self.lookahead() == '+':
            self.match('+')
            self.UNARY()
        elif self.lookahead() == '-':
            self.match('-')
            self.UNARY()
        else:
            self.FACTOR()

    def FACTOR(self):
        if self.lookahead() == '(':
            self.match('(')
            self.EXPR()
            self.match(')')
        elif self.lookahead().isdigit():
            self.match(self.lookahead())
        elif self.lookahead().isalpha():
            self.ACCESS()
        else:
            self.error(f"Esperado '(', dígito ou identificador, mas encontrado '{self.lookahead()}'")

    def ACCESS(self):
        if self.lookahead().isalpha():
            self.match(self.lookahead())  # consumindo o id (letra única)
            self.ACCESS_()
        else:
            self.error(f"Esperado identificador, mas encontrado '{self.lookahead()}'")

    def ACCESS_(self):
        if self.lookahead() == '[':
            self.match('[')
            self.EXPR()
            self.match(']')
        elif self.lookahead() == '(':
            self.match('(')
            self.ARGS()
            self.match(')')
        else:
            # ε (vazio)
            pass

    def ARGS(self):
        if self.lookahead() == ')' or self.lookahead() == self.EOF:
            # ε: sem argumentos
            pass
        else:
            self.ARG()
            self.ARGS_REST()

    def ARGS_REST(self):
        if self.lookahead() == ',':
            self.match(',')
            self.ARG()
            self.ARGS_REST()
        else:
            # ε
            pass

    def ARG(self):
        self.EXPR()
