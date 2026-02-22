frase = input("Digite uma frase: ")

texto_limpo = ""
for char in frase:
    if char.isalpha():
        texto_limpo += char.lower()

eh_palindromo = True
tamanho = len(texto_limpo)

for i in range(tamanho // 2):
    if texto_limpo[i] != texto_limpo[tamanho - 1 - i]:
        eh_palindromo = False
        break

if eh_palindromo:
    print(f"A frase é um palíndromo.")
else:
    print(f"A frase não é um palíndromo.")