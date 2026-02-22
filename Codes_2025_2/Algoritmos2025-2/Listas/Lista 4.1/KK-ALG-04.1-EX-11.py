N = int(input("digite o numero :"))
dividendo = 0
resposta = 0
while (dividendo) < N:
    dividendo = dividendo + 1
    if dividendo % 2 == 0:
        solucao = (resposta) - (1 / (dividendo))
        resposta = solucao
        print(resposta)
    else:
        solucao = (resposta) + (1 / (dividendo))
        resposta = solucao
        print(resposta)