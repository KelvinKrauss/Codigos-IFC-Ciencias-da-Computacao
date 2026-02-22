suco = float(input("valor do suco R$"))
prato = float(input("valor do prato principal R$"))
sobremesa = float(input("valor da sobremesa R$")) 
total = suco + prato + sobremesa
taxa = total * 0.10
valorfinal = total + taxa
print("o valor total da conta é de R$", format(valorfinal, '.2f'))