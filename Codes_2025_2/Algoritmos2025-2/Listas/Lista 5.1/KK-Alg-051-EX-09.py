def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        print(f"o ano {ano} é bissexto")
    else:
        print(f"o ano {ano} não é um ano bissexto")

ano = int(input("Digite o ano"))
eh_bissexto(ano)