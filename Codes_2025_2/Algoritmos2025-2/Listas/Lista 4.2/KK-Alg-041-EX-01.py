
import math
valores = []
infinito = math.inf
tamanho = 0
numeros = int(input("digite os valores"))
valores.append(numeros)
print(valores)
if valores [0] == 0:
    print("o primeiro valor nao pode ser 0")

while tamanho <= infinito:
    numeros = int(input("digite o numero: "))
    print(valores)
    valores.append(numeros)
    if any(x == 0 for x in valores[1:]):
        valores.remove(0)
        soma = sum(valores)
        tamanho = len(valores)
        media = soma / tamanho
        print(media)
        break