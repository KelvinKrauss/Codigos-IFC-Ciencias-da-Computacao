def encaixa(a, b):
    str_a = str(a)
    str_b = str(b)
    if len(str_b) > len(str_a):
        return False
    
    ultimo_segmento_a = str_a[len(str_a) - len(str_b):]
    
    return ultimo_segmento_a == str_b


resultado = {encaixa(int(input()),int(input()))}
if resultado == True:
    print("encaixa")
else:
    print("não encaixa")
