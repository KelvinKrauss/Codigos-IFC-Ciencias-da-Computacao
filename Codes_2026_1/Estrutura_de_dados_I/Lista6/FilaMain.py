from FilaVetor import FilaVetor

def main():
    guiche = FilaVetor(5)
    
    senhas = [101, 102, 103, 104, 105]
    for s in senhas:
        guiche.enqueue(s)
    
    try:
        guiche.enqueue(106)
    except Exception as e:
        print(e)
    
    print("Atendimento:", guiche.dequeue())
    guiche.enqueue(106)
    
    print("Fila atual:", guiche)
    
    guiche.reset()
    print("Fila vazia:", guiche)

    f1 = FilaVetor(3)
    for x in [3, 1, 5]: f1.enqueue(x)
    
    f2 = FilaVetor(5)
    for x in [7, 8, 2, 11, 6]: f2.enqueue(x)
    
    print("Concatena:", f1.concatena(f2))
    print("Merge:", f1.merge(f2))

if __name__ == "__main__":
    main()