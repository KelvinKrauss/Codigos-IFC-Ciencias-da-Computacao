num_str = input("Digite um número inteiro (maior ou igual a 2): ")
n = int(num_str)

if n < 2:
    print("Erro: O número deve ser maior ou igual a 2.")
else:
    fator = 2
    print(f"A fatoração de {n} é:")
    while fator <= n:
        if n % fator == 0:
            print(fator)
            n = n // fator
        else:
            fator += 1