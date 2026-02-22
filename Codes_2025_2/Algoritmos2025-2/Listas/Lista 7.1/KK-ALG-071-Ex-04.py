def diferenca(conjunto_a,conjunto_b):
    return conjunto_a - conjunto_b

def main():
    conjunto_a,conjunto_b, cjt_b = set(), set(), False
    while True:
        n_str = str(input("Digite os números do conjunto A, Enter para sair : "))
        if n_str == "":
            cjt_b = True
            break
        else:
            n = int(n_str)
            conjunto_a.add(n)
            
    if cjt_b == True:
        while True:
            n_str = str(input("Digite os números do conjunto B, Enter para sair : "))
            if n_str == "":
                break
            else:
                n = int(n_str)
                conjunto_b.add(n)
    print(diferenca(conjunto_a,conjunto_b))
    
main()