d = float(input("dia(s)"))
h = float(input ("hora(s)"))
m = float(input ("minuto(s)"))
s = float(input ("segundo(s)"))
sold = d * 24 * 60 * 60
solh = h * 60 * 60
solm = m * 60
s = s
solucao = sold + solh + solm + s
print ("os segundos sao", solucao)