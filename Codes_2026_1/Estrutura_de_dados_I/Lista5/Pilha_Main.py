from Calc import Calc
calc = Calc()

print("Digite os valores e operadores separados por espaço (ou 'q' para sair):")
print("Exemplo: 3 5 8 * + 7 / q")

#le tudo e separa
entrada = input().split()

for item in entrada:
    if item == 'q':
        break
    elif item == '+' or item == '-' or item == '*' or item == '/':
        calc.operador(item)
    else:
        #tenta transformar em float, se der erro ignora e continua
        try:
            valor = float(item)
            calc.operando(valor)
        except ValueError:
            pass
            
calc.libera()