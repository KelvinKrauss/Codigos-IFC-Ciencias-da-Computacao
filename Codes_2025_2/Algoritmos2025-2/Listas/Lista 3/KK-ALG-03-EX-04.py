lados = int(input("quantos lados tem o poligono? :"))
if lados > 10 or lados < 3:
    lados = ("NUMERO INVALIDO, insira um numero entre 3 e 10 ")
elif lados == 3:
    lados = ("Triangulo")
elif lados == 4:
    lados = ("Quadrado")
elif lados == 5:
    lados = ("Pentágono")
elif lados == 6:
    lados = ("Hexagono")
elif lados == 7:
    lados = ("Heptagono")
elif lados == 8:
    lados = ("Octogono")
elif lados == 9:
    lados = ("Eneagono")
elif lados == 10:
    lados = ("Decagono")    
    
print(f"o seu poligono é um {lados}")

