import random

total_de_sorteios = 0
num_simulacoes = 10

for i in range(num_simulacoes):
    sorteios = 0
    consecutivos = 0
    ultimo_resultado = ''
    saida = ""

    while consecutivos < 3:
        sorteios += 1
        if random.randint(0, 1) == 0:
            resultado_atual = 'A'
        else:
            resultado_atual = 'O'
        
        saida += resultado_atual
        
        if resultado_atual == ultimo_resultado:
            consecutivos += 1
        else:
            ultimo_resultado = resultado_atual
            consecutivos = 1
            
    print(f"{saida} ({sorteios} sorteios)")
    total_de_sorteios += sorteios

media = total_de_sorteios / num_simulacoes
print(f"Na média, foram necessários {media} sorteios.")