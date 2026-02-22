x_str = input("Digite um número para calcular a raiz quadrada: ")
x = float(x_str)

raiz = x / 2
precisao = 1e-12

while abs(raiz * raiz - x) >= precisao:
    raiz = (raiz + x / raiz) / 2

print(f"A raiz quadrada de {x} é aproximadamente {raiz}")