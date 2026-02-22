vi = float(input("digite o valor inicial na conta: R$ "))
juros = 0.12
sa1 = vi * (1 + juros)
sa2 = sa1 * (1 + juros)
sa3 = sa2 * (1 + juros)
print("dinheiro em 1 ano:R$", format(sa1, '.2f'))
print("dinheiro em 2 anos:R$", format(sa2, '.2f'))
print("dinheiro em 3 anos:R$", format(sa3, '.2f'))