def mediana(a,b,c):
        lista = [a, b, c]
        lista.sort()
        return lista[1]

def main(mediana):
        mediana = mediana(int(input("Digite A : ")),int(input("Digite B : ")),int(input("Digite C : ")))
        print(f"a mediana é {mediana}!")

main(mediana)