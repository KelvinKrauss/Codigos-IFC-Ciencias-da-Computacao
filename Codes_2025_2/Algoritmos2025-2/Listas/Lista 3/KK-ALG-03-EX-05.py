me = str(input("digite qual mes voce quer saber os dias :"))
mes = me.lower()
if mes == "janeiro":
    print("Janeiro tem 31 dias")
elif mes == "fevereiro":
    print("Fevereiro tem 28 ou 29 dias")
elif mes == "março" or "marco":
    print("Março tem 31 dias")
elif mes == "abril":
    print("Abril tem 30 dias")
elif mes == "maio":
    print("Maio tem 31 dias")
elif mes == "junho":
    print("Junho tem 30 dias")
elif mes == "julho":
    print("Julho tem 31 dias")
elif mes == "agosto":
    print("Agosto tem 31 dias")
elif mes == "setembro":
    print("Setembro tem 30 dias")
elif mes == "outubro":
    print("Outubro tem 31 dias")
elif mes == "novembro":
    print("Novembro tem 30 dias")
elif mes == "dezembro":
    print("Dezembro tem 31 dias")
else:
    print("invalido")
    