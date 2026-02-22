numeros = []
a = 1
while a > 0:
    
    entrada = (input("digite o numero"))
    if entrada == "" :
        break
    else :
        numerodigitado = int(entrada)
        numeros.append(numerodigitado)
        print(numeros)
numeromaximo = max(numeros)
numerominimo = min(numeros)
somadosnumerosdalista = sum(numeros)
quantidadedenum = len(numeros)
numeromedio = somadosnumerosdalista / quantidadedenum
print(f"o maior numero é {numeromaximo}, o menor numero é {numerominimo} e a média é {numeromedio} ")