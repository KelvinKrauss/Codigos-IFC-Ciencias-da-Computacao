def estatisticas_texto(texto):
    palavras = texto.lower().split()
    dicionario = {}
    
    for p in palavras:
        if p in dicionario:
            dicionario[p] += 1
        else:
            dicionario[p] = 1
            
    return set(dicionario.keys()), dicionario

texto = "o rato roeu a roupa do rei de roma o rato roeu a roupa do rei da russia"
unicas, contagem = estatisticas_texto(texto)

print(f"Total de palavras distintas: {len(unicas)}")

top_5 = sorted(contagem.items(), key=lambda item: item[1], reverse=True)[:5]
print(f"5 mais frequentes: {top_5}")