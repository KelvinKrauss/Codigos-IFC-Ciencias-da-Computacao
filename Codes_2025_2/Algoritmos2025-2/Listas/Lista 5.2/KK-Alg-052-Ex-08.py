def corrige_texto():
    prox_letra_m = True
    text = text.lower()
    texto = []
    for char in text:
        if prox_letra_m and char.isalpha():
            texto.append(char.upper())
            prox_letra_m = False
        elif char in "!.?":
            texto.append(char)
            prox_letra_m = True
        else:
            texto.append(char)
    textof = "".join(texto)
    print (textof)

def main():
    corrige_texto(str(input("Digite o texto para ser corrigido : ")))

main()