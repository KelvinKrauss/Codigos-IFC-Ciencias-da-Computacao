def countRange(lista,mini,maxi):
    lista_com_limites = []
    for i in range(len(lista)):
        if lista[i] >= mini and lista[i] < maxi:
            lista_com_limites.append(lista[i])
    return len(lista_com_limites)

def main():
    lista = []
    while True:
        n_str = str(input("Digite o número : "))
        if n_str == "":
            break
        else:
            n = float(n_str)
            lista.append(n)
        
    mini = float(input("Digite o limite minimo : "))
    maxi = float(input("Digite o limite máximo : "))
    lista_com_limites = countRange(lista,mini,maxi)
    print (lista_com_limites)
    
main()