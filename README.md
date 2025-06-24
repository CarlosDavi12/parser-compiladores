# Parser LL(1) - Gramática 3

Este projeto é um **analisador sintático preditivo descendente** (LL(1)) implementado em Python, desenvolvido como parte do **Trabalho I** da disciplina de **Compiladores** da UFOPA. O parser reconhece expressões aritméticas com operadores binários, unários, chamadas de funções e acesso a arranjos, conforme definido na **Gramática 3** proposta pelo professor Éfren L. Souza.

---

## Estrutura da Gramática (LL(1) ajustada)

```
EXPR       ::= TERM EXPR'
EXPR'      ::= + TERM EXPR' | - TERM EXPR' | ε
TERM       ::= UNARY TERM'
TERM'      ::= * UNARY TERM' | / UNARY TERM' | ε
UNARY      ::= + UNARY | - UNARY | FACTOR
FACTOR     ::= (EXPR) | digit | ACCESS
ACCESS     ::= id ACCESS'
ACCESS'    ::= [EXPR] | (ARGS) | ε
ARGS       ::= ARG ARGS_REST | ε
ARGS_REST  ::= , ARG ARGS_REST | ε
ARG        ::= EXPR
```

---

## Estrutura do Projeto

```
├── parser.py         # Implementação do parser
├── teste_parser.py   # Script de testes com exemplos válidos e inválidos
├── README.md         # Este arquivo
```

---

## Como executar

### 1. Tenha o Python 3 instalado

Você pode verificar com:

```bash
python --version
```

### 2. Execute os testes

No terminal ou prompt de comando, digite:

```bash
python teste_parser.py
```

---

## Exemplos de expressões válidas

- `(a + b) * c[3]`
- `f(1, x + 2, g(4)) - 7`
- `-((a + b[5]) / z)`

---

## Exemplos de expressões inválidas

- `a + * b` → operador mal posicionado  
- `f(1, )` → argumento vazio  
- `x[2` → colchete não fechado  
- `((a+b)` → parêntese não fechado

---

## Créditos

Trabalho desenvolvido por:

- Carlos Davi Gomes Pereira  
- Daniel Silva do Nascimento  
- Eduardo Batista Soares  
- Gabriel Camargo Neves

Disciplina de Compiladores – UFOPA  
Professor: Éfren L. Souza
