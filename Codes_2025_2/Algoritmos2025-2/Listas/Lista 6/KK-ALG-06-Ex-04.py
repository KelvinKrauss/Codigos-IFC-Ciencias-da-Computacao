def Remove_repetidos():
    lista = []
    while True:
        palavra = str(input("Digite a string : "))
        if palavra == "":
            break
        else:
            lista.append(palavra)
            if lista.count(palavra) > 1:
                del lista[len(lista) - 1]
    print ("\n".join(lista))

Remove_repetidos()