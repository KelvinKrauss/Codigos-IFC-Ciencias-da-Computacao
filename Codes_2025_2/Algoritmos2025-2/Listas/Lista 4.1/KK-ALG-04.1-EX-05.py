N = int(input("Digite um numero"))
D = 1
resultado = 0
A = 0
for y in range (N):
    A = N / D + A
    print(f"o resultado do passo a passo é {A}")
    D = D + 1
    N = N - 1
    
print(f"o resultado final é {A}")