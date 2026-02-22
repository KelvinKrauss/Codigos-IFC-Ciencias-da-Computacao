def numeros_ordinais(n):
    lista = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto", "Sexto", "Sétimo","Oitavo","Nono","Décimo", "Décimo Primeiro", "Décimo Segundo"]
    if n > 13 or n < 1:
        print("")
    else:
        print(lista[n - 1])

def main():
    numero = 1
    while numero <= 12:
        numeros_ordinais((numero))
        numero = numero + 1

main()