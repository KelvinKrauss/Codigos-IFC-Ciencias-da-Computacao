def valores_unicos(lista):
    lista_nova = set(lista)
    print(f"a lista sem duplicatas é \n {lista_nova}")
    
def main():
    lista = []
    while True:
        n = int(input("Digite o número, 0 para parar. "))
        if n == 0:
            break
        else:
            lista.append(n)
    valores_unicos(lista)

main()