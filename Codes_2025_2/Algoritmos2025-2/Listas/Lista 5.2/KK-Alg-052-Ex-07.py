def Triangulo_valido(a, b, c):
    if a >= b + c or b >= a + c or c >= b + a:
        Triangulo = False
    else:
        Triangulo = True
    return Triangulo

def user_input():
        print(Triangulo_valido(int(input("Digite o lado A : ")),int(input("Digite o lado B : ")),int(input("Digite o lado C : "))))
      
user_input()