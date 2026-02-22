def precedencia(op):
    if op in '+-':
        return 1
    elif op in '*/':
        return 2
    elif op in '^':
        return 3
    else:
        return -1
    
def main():
    op = str(input("Digite o operador : "))
    prec = precedencia(op)
    if prec > -1:
        print (prec)
    else:
        print ("Erro")
    
main()