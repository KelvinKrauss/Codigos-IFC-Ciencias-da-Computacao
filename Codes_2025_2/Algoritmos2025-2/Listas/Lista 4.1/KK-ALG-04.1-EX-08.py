numeros = []
a = 0
while a <= 10:
    a = a + 1
    numerodigitado = int(input("digite o numero"))
    numeros.append(numerodigitado)
    print(numeros)
    
numeromaximo = max(numeros)
numerominimo = min(numeros)
somadosnumerosdalista = sum(numeros)
quantidadedenum = len(numeros)
numeromedio = somadosnumerosdalista / quantidadedenum
print(f"o maior numero é {numeromaximo}, o menor numero é {numerominimo} e a média é {numeromedio} ")