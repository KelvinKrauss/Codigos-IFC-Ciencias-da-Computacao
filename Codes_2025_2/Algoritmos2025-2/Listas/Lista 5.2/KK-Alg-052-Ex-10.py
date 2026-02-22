def é_primo(n):#5
    dvsoes = 0
    for i in range(1,n + 1,1):#1,2,3,4,5
        if n % i == 0:
            dvsoes = dvsoes + 1
    if dvsoes == 2:
        return True
    else:
        return False

def main():
    bol = (é_primo(int(input("Digite o numero : "))))
    if bol == True:
        print ('É primo')
    else:
        print ('Não é primo')
    
main()