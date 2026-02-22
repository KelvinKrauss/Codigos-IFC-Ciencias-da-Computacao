def potencia(x, y):
    temp = x
    for _ in range (y -1):
        z = x * temp
        x = z
    return z

x = int(input("digite o numero : "))
y = int(input("digite o numero da Potencia :"))
print(f"{x} elevado a {y} é {potencia(x,y)}!")