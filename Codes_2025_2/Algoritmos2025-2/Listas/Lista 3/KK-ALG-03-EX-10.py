y = int(input("Digite a posição vertical :"))
x = str(input("digite a posição horizontal :"))
if y % 2 == 0 and x in ['a','c','e','g',]:
    print(f"o quadrado da posição {y}{x} é branco")
else:
    print(f"o quadrado da posição {y}{x} é preto")