codigos = [66, 65, 78, 257, 65, 256, 258, 258]

#Inicializa a tabela ASCII
dicionario = {i: chr(i) for i in range(256)}
prox_cod = 256

#Pega o primeiro
w = dicionario[codigos.pop(0)]
saida = [w]

for k in codigos:
    if k in dicionario:
        entry = dicionario[k]
    elif k == prox_cod:
        entry = w + w[0]
    
    saida.append(entry)

    #Lógica de reconstrução do dicionario
    wc = w + entry[0]
    dicionario[prox_cod] = wc
    
    print(f"Criado {prox_cod}: {wc}")

    prox_cod += 1
    w = entry

print("Final: " + ''.join(saida))