Numero = int(input("Digite o valor de N"))
if Numero < 0 :
    print("O numero temque ser positivo")
else:
    inducao = 0
    for i in range (1, Numero + 1):
        inducao += 1/i
        print(inducao)