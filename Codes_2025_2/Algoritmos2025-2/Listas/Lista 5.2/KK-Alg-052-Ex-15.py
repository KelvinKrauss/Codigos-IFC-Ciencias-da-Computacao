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
        
resposta1 = hex2int(str(input("Digito Hexadecimal : ")))
print(resposta1)
resposta2 = int2hex(int(input("Digito Decimal : ")))
print(resposta2)