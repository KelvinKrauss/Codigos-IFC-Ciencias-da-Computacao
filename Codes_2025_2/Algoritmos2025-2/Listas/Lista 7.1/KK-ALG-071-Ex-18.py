def palavras_unicas(frases):
    contagem = {}
    for conjunto_palavras in frases.values():
        for palavra in conjunto_palavras:
            contagem[palavra] = contagem.get(palavra, 0) + 1
    resultado = set()
    for palavra,qtd in contagem.items():
        if qtd >= 2:
            resultado.add(palavra)
    return resultado

frases = {
    "frase1" : {"pão", "trigo", "cevada"},
    "frase2" : {"vinho", "trigo", "cevada"},
    "frase3" : {"terra", "trigo", "agua"}
}

print(palavras_unicas(frases))