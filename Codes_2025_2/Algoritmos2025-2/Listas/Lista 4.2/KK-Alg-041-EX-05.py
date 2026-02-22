resultado = False
pr = 0
numero = 0
palavra = (numero)
while resultado == False:
    numero = numero + 1
    palavra = str(numero) + "°"
    idatexto = str(input(f"Digite a {palavra} idade :"))
    if idatexto == (""):
        resultado = True
    else:
        ida = int(idatexto)
        if ida >= 3 and ida <= 12:
            pr = pr + 14
        elif ida >= 13 and ida <= 64:
            pr = pr + 23
        elif ida >= 65:
            pr = pr + 18
        else:
            pr
            
print(f"{pr},00 R$ é o valor total dos ingressos!")