def uniao(a, b):
    return a | b

def main():
    conjunto_a = set()
    while True:
        n_str = input("Digite um número (ou Enter para parar): ")
        if n_str == "":
            break
        else:
            conjunto_a.add(int(n_str))

    conjunto_b = set()
    while True:
        n_str = input("Digite um número (ou Enter para parar): ")
        if n_str == "":
            break
        else:
            conjunto_b.add(int(n_str))

    conjunto_uniao = uniao(conjunto_a, conjunto_b)
    tamanho = len(conjunto_uniao)
    print("\nConjunto União:", conjunto_uniao)
    print(f"Tamanho do Conjunto: {tamanho}") 

main()