def tokenizar(s):
    tokens = []
    i = 0
    while i < len(s):
        char = s[i]

        if char.isspace():
            i += 1
            continue

        if char in "*/^()":
            tokens.append(char)
            i += 1
        elif char == "+" or char == "-":
            j = i - 1
            ultimo_nao_espaco = ""
            while j >= 0:
                if not s[j].isspace():
                    ultimo_nao_espaco = s[j]
                    break
                j -= 1

            if ultimo_nao_espaco.isdigit() or ultimo_nao_espaco == ")":
                tokens.append(char)
                i += 1
            else:
                num_str = char
                i += 1
                while i < len(s) and s[i].isdigit():
                    num_str += s[i]
                    i += 1
                tokens.append(num_str)
        elif char.isdigit():
            num_str = char
            i += 1
            while i < len(s) and s[i].isdigit():
                num_str += s[i]
                i += 1
            tokens.append(num_str)
        else:
            i += 1
            
    return tokens

def infixo_para_posfixo(tokens):
    precedencia = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }
    
    posfixa = []
    operadores = []
    
    for token in tokens:
        if (token.isdigit() or 
            (token[0] == '-' and len(token) > 1 and token[1:].isdigit()) or
            (token[0] == '+' and len(token) > 1 and token[1:].isdigit())):
            posfixa.append(token)
        elif token == '(':
            operadores.append(token)
        elif token == ')':
            while operadores and operadores[-1] != '(':
                posfixa.append(operadores.pop())
            operadores.pop()
        elif token in precedencia:
            while (operadores and 
                   operadores[-1] != '(' and 
                   precedencia[operadores[-1]] >= precedencia[token]):
                posfixa.append(operadores.pop())
            operadores.append(token)
            
    while operadores:
        posfixa.append(operadores.pop())
        
    return posfixa

def avaliar_posfixo(tokens_posfixos):
    valores = []
    
    for token in tokens_posfixos:
        if (token.isdigit() or 
            (token[0] == '-' and len(token) > 1 and token[1:].isdigit()) or
            (token[0] == '+' and len(token) > 1 and token[1:].isdigit())):
            valores.append(int(token))
        elif token in "+-*/^":
            operando_direita = valores.pop()
            operando_esquerda = valores.pop()
            
            resultado = 0
            if token == '+':
                resultado = operando_esquerda + operando_direita
            elif token == '-':
                resultado = operando_esquerda - operando_direita
            elif token == '*':
                resultado = operando_esquerda * operando_direita
            elif token == '/':
                resultado = operando_esquerda / operando_direita
            elif token == '^':
                resultado = operando_esquerda ** operando_direita
            
            valores.append(resultado)
            
    return valores[0]

#programa principal
expressao_infixa = input("Digite uma expressão matemática infixa: ")

tokens_infixos = tokenizar(expressao_infixa)
tokens_posfixos = infixo_para_posfixo(tokens_infixos)
valor = avaliar_posfixo(tokens_posfixos)

print("O resultado da expressão é: ", valor)