binario_str = input("Digite um número binário: ")

decimal = 0
for digito in binario_str:
    decimal = decimal * 2 + int(digito)

print(f"O equivalente decimal é: {decimal}")