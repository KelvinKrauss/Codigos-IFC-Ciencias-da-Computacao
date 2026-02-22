N = int(input("Digite o numero"))
solucao = 0
dividendo = 3
solucao = 1 + (1 / (dividendo))
resultado = solucao
print(solucao)
while dividendo < (N):
    dividendo = dividendo + 2
    solucao = resultado + (1 / (dividendo))
    resultado = solucao
    print(resultado)