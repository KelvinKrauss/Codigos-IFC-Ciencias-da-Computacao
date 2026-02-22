def lista():
    lista = []
    while True:
        n = int(input("Digite um número inteiro: "))
        if n == 0:
            break
        else:
            lista.append(n)
    lista = bubble_sort(lista)
    for i in range(len(lista)):
        print (lista[i])

def bubble_sort(lista):
    tamanho = len(lista)
    for x in range(tamanho):
        swapped = False
        for i in range(0, tamanho - x - 1):
            if lista[i] > lista[i + 1]:
               lista[i], lista[i + 1] = lista[i + 1], lista[i]
               swapped = True

        if not swapped:
            break

    return lista

lista()