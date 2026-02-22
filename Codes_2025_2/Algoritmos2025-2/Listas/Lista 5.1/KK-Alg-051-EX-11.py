def conta_digitos(n, d):
    quantidade = 0
    str_n = str(n)
    str_d = str(d)
    for digito_char in str_n:
        if digito_char == str_d:
            quantidade += 1
    return quantidade

a,b = int(input("Digite o primeiro inteiro positivo (a): ")),int(input("Digite o segundo inteiro positivo (b): "))
if a <= 0 or b <= 0:
    print("Por favor, insira apenas inteiros positivos.")

permutacao = True
if len(str(a)) != len(str(b)):
    permutacao = False
else:
    for d in range(1, 10):
        if conta_digitos(a, d) != conta_digitos(b, d):
            is_permutation = False
            break

if permutacao:
    print(f"\nSim, {a} é uma permutação de {b}.")
else:
    print(f"\nNão, {a} não é uma permutação de {b}.")
