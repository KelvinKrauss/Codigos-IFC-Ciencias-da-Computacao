v1 = int(input("quantos vasilhames de 1 litro ou menos: "))
v2 = int(input("quantos vasilhames de mais de 1 litro: "))
c1 = v1 * 0.10 
c2 = v2 * 0.25
total = c1 + c2
print("o valor total de R$", format(total, '.2f'))   
