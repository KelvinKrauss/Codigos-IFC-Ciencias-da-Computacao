def Centralizando_String(texto, largura):
    largura_str = (" " * (largura // 2))
    texto_total = largura_str + texto + largura_str
    return texto_total

def main():
    texto = Centralizando_String(str(input("Digite o texto para centralizar : ")),int(input("Digite a Largura : ")))
    print(texto)

main()