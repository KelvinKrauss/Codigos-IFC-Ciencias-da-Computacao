def Abaixo_e_acima_da_média():
    numeros = []
    terminou = False
    while True:
        n_str = str(input("Digite o número : "))
        if n_str == "":
            media = sum(numeros) / len(numeros)
            print(f"A média é {media}")
            terminou = True
            break
        else:
            n = float(n_str)
            numeros.append(n)
            
    if terminou == True:
        n_menor_que_media,n_igual_media,n_maior_que_media = [],[],[]
        for p in range (len(numeros)):
            if numeros[p] < media:
                n_menor_que_media.append(numeros[p])
            elif numeros[p] == media:
                n_igual_media.append(numeros[p])
            elif numeros[p] > media:
                n_maior_que_media.append(numeros[p])
            
    print(f"Números Abaixo da média : \n{n_menor_que_media}")
    print(f"Números na média : \n{n_igual_media}")
    print(f"Números acima da média : \n{n_maior_que_media}")
    
Abaixo_e_acima_da_média()