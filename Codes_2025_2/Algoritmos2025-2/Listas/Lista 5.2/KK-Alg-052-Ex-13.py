def Dias_em_um_mês(mes,ano):
    if mes > 0 and mes <= 12 and ano >= 0 and ano <= 9999:
        mes_com_31_dias = (1,3,5,7,8,10,12)
        mes_com_30_dias = (4,6,9,11)
        if mes in mes_com_31_dias:
            return 31
        elif mes in mes_com_30_dias:
            return 30
        elif mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                return 29
            else:
                return 28
                
def main():
    mes = Dias_em_um_mês(int(input("Digite o mês no formato 00 : ")),int(input("Digite o ano no formato 0000 : ")))
    print(f"o mês tem {mes} dias")
    
main()