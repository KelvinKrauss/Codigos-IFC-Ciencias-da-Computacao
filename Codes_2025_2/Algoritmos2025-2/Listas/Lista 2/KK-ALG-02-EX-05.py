centavos = int(input("digite o valor do troco em centavos : "))
moedas = [50, 25, 10, 5, 1]
for moeda in moedas:
    qtd = centavos // moeda
    centavos %= moeda
    if qtd > 0:
        print(f"{qtd} moeda(s) de {moeda} centavo(s)")