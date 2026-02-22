entrada = "BANANABANANA"
#Inicializa com os 256 caracteres ASCII padrão, w = word, c = character
dicionario = {chr(i): i for i in range(256)}
prox_cod = 256

w = ""
saida = []

for c in entrada:
    wc = w + c
    if wc in dicionario:
        w = wc
    else:
        saida.append(dicionario[w])

        dicionario[wc] = prox_cod
        print(f"Código {prox_cod} criado para: '{wc}'")
        
        prox_cod += 1
        w = c

if w:
    saida.append(dicionario[w])

print("\n")
print(f"Saída Final: {saida}")