palavra = input("Digite uma palavra: ")

eh_palindromo = True
tamanho = len(palavra)

for i in range(tamanho // 2):
    if palavra[i] != palavra[tamanho - 1 - i]:
        eh_palindromo = False
        break

if eh_palindromo:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")