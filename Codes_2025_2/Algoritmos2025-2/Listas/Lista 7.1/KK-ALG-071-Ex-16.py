def traduzir(palavra, dicionario):
    if palavra in dicionario:
        return dicionario[palavra]
    

dicionario = {
    "praia" : "beach",
    "arvore" : "tree",
    "areia" : "sand"
}
palavra = "arvore"

print(traduzir(palavra,dicionario))