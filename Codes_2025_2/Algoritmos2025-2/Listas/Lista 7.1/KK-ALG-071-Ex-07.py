def eh_subconjunto(a,b):
    if a.issubset(b):
        return True
    else:
        return False
    
def main():
    conjunto_a = set()
    while True:
        n_str = input("Digite um número para o conjunto A(ou Enter para parar): ")
        if n_str == "":
            break
        else:
            conjunto_a.add(int(n_str))

    conjunto_b = set()
    while True:
        n_str = input("Digite um número para o conjunto B(ou Enter para parar): ")
        if n_str == "":
            break
        else:
            conjunto_b.add(int(n_str))
    é_sub = eh_subconjunto(conjunto_a,conjunto_b)
    print(é_sub)

main()