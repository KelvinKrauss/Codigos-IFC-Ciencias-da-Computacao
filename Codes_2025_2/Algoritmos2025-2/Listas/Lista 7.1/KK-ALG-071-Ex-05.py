import random

def numeros_unicos(qnt, limite):
    num_unicos = set()
    for _ in range(qnt):
        n = random.randint(1,limite)
        num_unicos.add(n)
    return num_unicos

def main():
    limite = int(input("Digite o limite : "))
    qnt = int(input("Digite a quantidade de números a serem sorteados : "))
    print(numeros_unicos(qnt,limite))

main()