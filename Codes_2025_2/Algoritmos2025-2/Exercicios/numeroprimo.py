def eh_palindromo(palavra):
    str_inv = palavra[-1:-(len(palavra)):-1]
    if palavra == str_inv:
        return True
    else:
        return False
    
eh_palindromo("ovo")