import math

lat1 = float(input("latitude ponto 1 (em graus): "))
lon1 = float(input("longitude ponto 1 (em graus): "))
lat2 = float(input("latitude ponto 2 (em graus): "))
lon2 = float(input("longitude ponto 2 (em graus): "))
t1 = math.radians(lat1)
g1 = math.radians(lon1)
t2 = math.radians(lat2)
g2 = math.radians(lon2)
distancia = 6371.01 * math.acos(
    math.sin(t1) * math.sin(t2) +
    math.cos(t1) * math.cos(t2) * math.cos(g1 - g2)
)
print(f"distancia entre os pontos: {distancia:.2f} km")
