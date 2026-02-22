def mapa_letras(palavra):
    contador = {}
    for letra in palavra:
        if letra in contador:
            contador[letra] = contador[letra] + 1
        else:
            contador[letra] = 1
    return contador

print(mapa_letras("biscoito"))