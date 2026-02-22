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

expressao = input("Digite uma expressão matemática: ")
tokens = tokenizar(expressao)
print("Os tokens são:", tokens)