def hex2int(hexa):
    hexa = hexa.upper()
    caracteres_hexa = ["A","B","C","D",'E','F']
    if hexa in "0123456789":
        return int(hexa)
    elif hexa in caracteres_hexa:
        posicao = caracteres_hexa.index(hexa)
        return (posicao + 10)
    else:
        return False

def int2hex(decimal):
    valores_hex = ("A,B,C,D,E,F")
    valores_hex = valores_hex.split(",")
    decimal_numero = int(decimal)
    if decimal_numero <=9:
        return str(decimal)
    elif decimal_numero >= 10 and decimal_numero <= 15:
        return str(valores_hex[decimal_numero - 10])
    else:
        return False
    
def b_para_dec(n, b):
    dec = 0
    tam = len(n)
    for i in range(tam):
        d = hex2int(n[i])
        dec = dec + d * b**(tam-1-i)
    return dec

def dec_para_b(n_dec,b):
    if b < 2 or b > 16:
        print("Erro, Base inválida ")
        return None
    if n_dec == 0:
        return "0"
    resultado_str = ""
    while n_dec > 0:
        resto = n_dec % b
        n_dec = n_dec//b
        digito = int2hex(resto)
        resultado_str = digito + resultado_str
    return resultado_str

def main():
    num_origem = input("Digite o número a ser convertido para decimal: ")
    base_origem = int(input(f"Digite a base de '{num_origem}' (2-16): "))
    resultado_dec = b_para_dec(num_origem, base_origem)
    
    if resultado_dec is not None:
        print(f"'{num_origem}' (base {base_origem}) é {resultado_dec} (base 10).\n")
    
    num_dec = int(input("Digite o número decimal a ser convertido: "))
    base_destino = int(input(f"Digite a base de destino (2-16) para '{num_dec}': "))
    resultado_base = dec_para_b(num_dec, base_destino)
    
    if resultado_base is not None:
        print(f"'{num_dec}' (base 10) é {resultado_base} (base {base_destino}).")
    
main()