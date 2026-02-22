numero = int(input("digite um numero de 3 digitos: "))
c = numero // 100
d = (numero % 100) // 10
u = numero % 10
print("centena:", c)
print("dezena:", d)
print("unidade:", u)