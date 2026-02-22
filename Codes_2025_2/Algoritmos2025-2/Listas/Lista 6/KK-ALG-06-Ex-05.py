def Negativos_zeros_e_positivos():
    lista_0,lista_positivos,lista_negativos = [],[],[]
    while True: 
        n = str(input("Digite o número : "))
        if n == "":
            break
        else:
            n_i = int(n)
            if n_i < 0:
                lista_negativos.append(n)
            elif n_i == 0:
                lista_0.append(n)
            else:
                lista_positivos.append(n)
    print("\n".join(lista_negativos))
    print("\n".join(lista_0))
    print("\n".join(lista_positivos))

Negativos_zeros_e_positivos()