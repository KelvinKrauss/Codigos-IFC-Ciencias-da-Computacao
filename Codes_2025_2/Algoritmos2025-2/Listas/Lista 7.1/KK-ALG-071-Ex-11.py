def converter_moeda(valor_em_reais, codigo):
    codigo = codigo.upper()
    dicionario = {
        "USD" : 5.00,
        "EUR" : 5.40,
        "ARS" : 0.025,
    }
    if codigo in dicionario:
        taxa_conversao = dicionario[codigo]
        valor_convertido = valor_em_reais / taxa_conversao
        return valor_convertido
    else:
        return None

def main():
    valor = float(input("Digite o valor : "))
    codigo = str(input("Digite o código da moeda(USD,EUR,ARS): "))
    valor_em_reais = converter_moeda(valor,codigo)
    print(valor_em_reais)
    
main()