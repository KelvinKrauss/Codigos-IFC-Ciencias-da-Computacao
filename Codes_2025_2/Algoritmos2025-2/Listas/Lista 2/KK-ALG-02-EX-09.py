data_texto = input("digite a data no formato DDMMAA: ")
dia = data_texto[0:2]
mes = data_texto[2:4]
ano = data_texto[4:6]
data_invertida_texto = ano + mes + dia

print(data_invertida_texto)