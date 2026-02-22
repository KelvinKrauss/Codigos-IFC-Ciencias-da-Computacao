def esta_ordenada(lista):
    if lista == sorted(lista) or lista == sorted(lista, reverse = True):
        return True
    else:
        return False
    
def main():
    lista = []
    while True:
        n_str = str(input("Digite o número : "))
        if n_str == "":
            break
        else:
            n = float(n_str)
            lista.append(n)
    print(esta_ordenada(lista))

main()    