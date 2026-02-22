import math

a = float(input("digite o valor de a :"))
b = float(input("digite o valor de b :"))
c = float(input("digite o valor de c :"))
solucao = (b ** 2) - (4 * a * c)
if solucao < 0:
    print("Não tem raiz")
elif solucao == 0:
    x = -b / (2 * a)
    print(f"a raiz unica é: {x}")
else:
    x1 = (-b + math.sqrt(solucao)) / (2 * a)
    x2 = (-b - math.sqrt(solucao)) / (2 * a)
    print(f"raiz 1 é {x1}")
    print(f"raiz 2 é {x2}")