def sorteia_mega():
    import random
    sorteados = []
    while len(sorteados) < 6:
        n = random.randint(1, 60)
        if n not in sorteados:
            sorteados.append(n)
            sorteados.sort()
    print(sorteados)
    
sorteia_mega()