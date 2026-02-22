year = int(input("digite um ano: "))

é_bissexto = False

if year % 400 == 0:
    é_bissexto = True

elif year % 100 == 0:
    é_bissexto = False

elif year % 4 == 0:
    é_bissexto = True

else:
    é_bissexto = False

if é_bissexto:
    print(f"{year} é ano bissexto")
else:
    print(f"{year} não é ano bissexto")