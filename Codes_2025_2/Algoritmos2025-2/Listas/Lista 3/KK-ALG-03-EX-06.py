l1 = float(input("digite o lado 1 do triangulo"))
l2 = float(input("digite o lado 2 do triangulo"))
l3 = float(input("digite o lado 3 do triangulo"))
if l1 == l2 == l3:
    print("se trata de um triangulo equilatero")
elif l1 == l2 and l2 != l3 or l1 == l3 and l1 != l2 or l2 == l3 and l3 != l1:
    print("se trata de um triangulo isóceles")
elif l1 != l2 != l3:
    print("se trata de um triangulo escaleno")