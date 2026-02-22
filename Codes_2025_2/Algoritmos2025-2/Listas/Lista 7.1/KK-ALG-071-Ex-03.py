def intersecao(conjunto_a,conjunto_b):
    print (conjunto_a & conjunto_b)
    
def main():
    nome_cjt = "A"
    conjunto_a,conjunto_b,cjt_b = set(), set(), False
    while True:
        if cjt_b == True:
            nome_cjt = "B"
        n_str = str(input(f"Conjunto {nome_cjt} - Digite o número, ou Enter para parar : "))
        if n_str == "":
            cjt_b = True
            if n_str == "" and cjt_b == True and len(conjunto_b) > 1:
                break
        else:
            n = int(n_str)
            if cjt_b == True:
                conjunto_b.add(n)
            else:
                conjunto_a.add(n)
    intersecao(conjunto_a,conjunto_b)

main()