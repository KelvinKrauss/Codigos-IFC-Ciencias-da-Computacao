def is_data_magica(dia,mes,ano):
    ano_str = str(ano)
    numero_a_comparar = dia * mes
    numero_a_comparar_str = str(numero_a_comparar)
    ano_sem_zero = ano_str[2:].lstrip('0')
    if numero_a_comparar_str == ano_sem_zero:
        return True
    else:
        return False

def is_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def Dias_em_um_mês(mes,ano):
    mes_com_31_dias,mes_com_30_dias= (1,3,5,7,8,10,12),(4,6,9,11)
    if mes in mes_com_31_dias:
        return 31
    elif mes in mes_com_30_dias:
        return 30
    elif mes == 2:
        if is_bissexto(ano):
            return 29
        else:
            return 28
    
def main():
    for ano in range (1901,2001):
        for mes in range (1,13):
            dias_no_mes_atual = Dias_em_um_mês(mes, ano)
            for dia in range(1, dias_no_mes_atual + 1):
                 if is_data_magica(dia,mes,ano):
                    print(f"{dia}/{mes}/{ano} é data magica!")
        
main()