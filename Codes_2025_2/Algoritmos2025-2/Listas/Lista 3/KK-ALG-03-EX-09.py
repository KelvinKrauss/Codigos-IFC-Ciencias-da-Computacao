dia = int(input("digite o dia no formato dd :"))
mes = int(input("digite o mes no formato mm :"))
if dia == 1 and mes == 1:
    print("Dia da contraternização universal! ")
elif dia == 21 and mes == 4:
    print("Dia de Tiradentes")
elif dia == 1 and mes == 5:
    print("Dia do Trabalhador")
elif dia == 7 and mes == 9:
    print("Dia de nossa senhora")
elif dia == 2 and mes == 11:
    print("Dia de Finados")
elif dia == 15 and mes == 11:
    print("dia da Proclamação da Republica")
elif dia == 25 and mes == 12:
    print("É NATAL!")
else :
    print("o dia e o mês informados não correspondem a um feriado nacional")