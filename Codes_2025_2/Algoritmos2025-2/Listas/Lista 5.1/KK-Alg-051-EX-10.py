def conta_digitos(n, d):
    quantidade = 0
    str_n = str(n)
    str_d = str(d)
    for digito_char in str_n:
        if digito_char == str_d:
            quantidade += 1
    return quantidade


numero_n = int(input("Digite um número : "))
digito_d = int(input("Digite o dígito a ser contado (d, entre 1 e 9): "))
if not (0 < digito_d <= 9):
    print("O dígito 'd' deve ser um valor entre 1 e 9.")
else:
    resultado = conta_digitos(numero_n, digito_d)
    print(f"\nO dígito {digito_d} aparece {resultado} vez(es) no número {numero_n}.")