valor = int(input("Digite o preço original do produto"))
desconto = 60
valordesconto = (valor * desconto) / 100
valoraposdesconto = valor - valordesconto
print(f"Valor Original\tDesconto\tValor após desconto")
print(f"{valor}\t\t{valordesconto}\t\t{valoraposdesconto}")