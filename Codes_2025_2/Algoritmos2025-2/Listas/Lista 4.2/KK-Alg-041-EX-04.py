import math

perimetro = 0.0

x_str = input("Digite a coordenada x de um ponto: ")
y_str = input("Digite a coordenada y de um ponto: ")

x_inicial = float(x_str)
y_inicial = float(y_str)

x_anterior = x_inicial
y_anterior = y_inicial

while True:
    x_str = input("Digite a coordenada x de um ponto (enter para sair): ")
    if x_str == "":
        break
    
    y_str = input("Digite a coordenada y de um ponto: ")
    
    x_atual = float(x_str)
    y_atual = float(y_str)
    
    distancia = math.sqrt((x_atual - x_anterior)**2 + (y_atual - y_anterior)**2)
    perimetro += distancia
    
    x_anterior = x_atual
    y_anterior = y_atual

distancia_final = math.sqrt((x_inicial - x_anterior)**2 + (y_inicial - y_anterior)**2)
perimetro += distancia_final

print(f"O perímetro deste polígono é igual a {perimetro}")