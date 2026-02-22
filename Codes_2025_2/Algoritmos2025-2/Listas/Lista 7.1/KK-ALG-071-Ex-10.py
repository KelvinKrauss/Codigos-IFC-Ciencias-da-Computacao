def contar_palavras(frase):
    frase = frase.lower().split()
    contagems = {}
    for palavra in frase:
        if palavra in contagems:
            contagems[palavra] = contagems[palavra] + 1
        else:
            contagems[palavra] = 1
    print(contagems)
    return contagems

contar_palavras("o rato")