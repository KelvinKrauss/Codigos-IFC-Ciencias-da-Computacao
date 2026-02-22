d = int(input("Quantos Decibeis? :"))
if d == 130:
    print("Britadeira")
elif d < 130 and d > 106:
    print("Entre Britadeira e Cortador de grama")
elif d == 106:
    print("Cortador de grama")
elif d < 106 and d > 70:
    print("entre Cortador de grama e Despertador")
elif d == 70:
    print("Despertador")
elif d == 40:
    print("Sala silenciosa")
elif d < 70 and d > 40:
    print("entre Despertador e Sala silenciosa")
elif d < 40:
    print("muito baixo")
elif d > 130:
    print("muito alto")