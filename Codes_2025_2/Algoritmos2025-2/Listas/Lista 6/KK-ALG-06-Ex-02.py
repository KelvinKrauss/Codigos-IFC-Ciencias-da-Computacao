import random

def lista():
    lista = []
    while True:
        n = int(input("Digite um número inteiro ou 0 para parar: "))
        if n != 0:
            lista.append(n)
        else:
            break
    lista = Bogo_Sort(lista)
    for i in range(len(lista)):
        print(lista[i])
    
def Bogo_Sort(lista):   # o fato do bogo sort usar aleatoriedade para organizar é interessante
    tamanho = len(lista)# mais de 15 numeros vai levar algumas decadas

    while True:
        esta_em_ordem = True
        for i in range(0,tamanho - 1):
            if lista[i] < lista[i + 1]:
                esta_em_ordem = False
                break

        if esta_em_ordem:
            return lista

        random.shuffle(lista)

lista()