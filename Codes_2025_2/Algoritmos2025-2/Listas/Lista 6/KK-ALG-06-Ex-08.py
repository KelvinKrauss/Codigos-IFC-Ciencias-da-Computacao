def Somente_Palavras(txt):
    lista = []
    for letra in range(len(txt)):
        if txt[letra] in "!?,":
            continue
        else:
            lista.append(txt[letra])
            txt2 = "".join(lista)
            lista_pronta = txt2.split()
    return(lista_pronta)

def main():
    txt = ("Beleza! Este é um ótimo Exemplo, você não acha?")
    lista_pronta = Somente_Palavras(txt)
    print(lista_pronta)
    
main()