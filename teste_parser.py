from parser import Parser 

def testar(expressao):
    try:
        p = Parser(expressao)
        p.parse()
        print(f"Expressão válida: {expressao}")
    except SyntaxError as e:
        print(f"Erro na expressão '{expressao}': {e}")

# Testes válidos
testar("(a + b) * c[3]")
testar("f(1, x + 2, g(4)) - 7")
testar("-((a + b[5]) / z)")

# Testes inválidos (para testar o erro)
testar("a + * b")         # operador mal posicionado
testar("f(1, )")          # vírgula sem argumento depois
testar("x[2")             # colchete não fechado
testar("((a+b)")          # parêntese não fechado
