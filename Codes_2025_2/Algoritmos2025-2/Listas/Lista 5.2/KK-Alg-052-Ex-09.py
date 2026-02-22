def isInteger(n):
    numeros = "0","1","2","3","4","5","6","7","8","9"
    sinais = "+","-"
    n_limpo = n.strip()
    if len(n_limpo) == 0:
        return False
    if len(n_limpo) <= 1:
        if n_limpo[0] in sinais:
            return False
    if n_limpo[0] in sinais or n_limpo[0] in numeros:
        for n in n_limpo[1:]:
            if n in numeros:
                continue
            else:
                return False
        return True
    else:
        return False

def main():
    print(isInteger(str(input())))
    
main()