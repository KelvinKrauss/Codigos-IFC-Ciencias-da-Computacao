def is_senha_valida(senha):
    if len(senha) >= 8:
        l_upper,l_lower,l_digit = False,False,False
        for c in senha:
            if c.isupper():
                l_upper = True
            elif c.islower():
                l_lower = True
            elif c.isdigit():
                l_digit = True
        if l_upper == True and l_lower == True and l_digit == True:
            return True
        else:
            return False
    else:
        return False
               
def main(): 
    print(is_senha_valida(str(input("Digite sua Senha : "))))
    
main()