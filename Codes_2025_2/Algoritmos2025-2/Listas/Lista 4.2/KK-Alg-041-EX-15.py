decimal_str = input("Digite um número decimal: ")
q = int(decimal_str)
result = ""

if q == 0:
    result = "0"
else:
    while q > 0:
        r = q % 2
        result = str(r) + result
        q = q // 2

print(f"O equivalente binário é: {result}")