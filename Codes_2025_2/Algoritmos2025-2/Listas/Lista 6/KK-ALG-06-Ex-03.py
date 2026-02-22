def removendo_extremos(lista,extremos):

    if len(lista) < extremos * 2:
        print(f"Erro: A lista precisa de pelo menos {extremos * 2} elementos.")
        return []
    else:
        lista_nova = sorted(lista)
        del lista_nova[0:extremos]
        del lista_nova[-extremos:]
        return lista_nova
    

def main():
    lista = []
    extremos = int(input("Digite a quantidade de extremos a remover de cada lado: "))

    while True:
        n_str = input("Digite um número (ou pressione Enter para terminar): ")
        if n_str == '':
            break
        else:
            n = int(n_str)
            lista.append(n)

    lista2 = removendo_extremos(lista,extremos)
    
    print("\nLista Original:", lista)
    print("Lista Modificada:", lista2)

main()