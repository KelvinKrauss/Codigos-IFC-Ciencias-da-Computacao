import time
import random
#Todas as atividades foram feitas no mesmo arquivo usando modularização
def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                trocou = True
        if not trocou:
            break

def quick_sort(vetor, inicio, fim):
    if inicio < fim:
        p = particao(vetor, inicio, fim)
        quick_sort(vetor, inicio, p - 1)
        quick_sort(vetor, p + 1, fim)

def particao(vetor, inicio, fim):
    pivo = vetor[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if vetor[j] <= pivo:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
    vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]
    return i + 1

def merge_sort(vetor):
    if len(vetor) > 1:
        meio = len(vetor) // 2
        esquerda = vetor[:meio]
        direita = vetor[meio:]
        
        merge_sort(esquerda)
        merge_sort(direita)
        
        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1
            
        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1
            
        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1

def gerar_vetor(n):
    vetor = list(range(1, n + 1))
    random.shuffle(vetor)
    return vetor

def principal():
    tamanhos = [10, 100, 1000, 10000]
    
    print("Resultados dos Tempos de Execução (em segundos):")
    print("Tamanho | BubbleSort | QuickSort | MergeSort")
    print("-" * 50)
    
    for n in tamanhos:
        dados = gerar_vetor(n)
        
        # Fazendo copias para ordenar o mesmo vetor nos tres algoritmos
        v_bubble = dados.copy()
        v_quick = dados.copy()
        v_merge = dados.copy()
        # Tempo BubbleSort
        t0 = time.time()
        bubble_sort(v_bubble)
        tempo_bubble = time.time() - t0
        
        # Tempo QuickSort
        t0 = time.time()
        quick_sort(v_quick, 0, len(v_quick) - 1)
        tempo_quick = time.time() - t0
        
        # Tempo MergeSort
        t0 = time.time()
        merge_sort(v_merge)
        tempo_merge = time.time() - t0
        
        print(f"{n:<7} | {tempo_bubble:.5f}    | {tempo_quick:.5f}   | {tempo_merge:.5f}")

if __name__ == "__main__":
    principal()
