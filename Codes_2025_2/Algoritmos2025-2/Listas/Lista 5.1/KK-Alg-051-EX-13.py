def encaixa(a, b):
    str_a = str(a)
    str_b = str(b)
    if len(str_b) > len(str_a):
        return False
    ultimo_segmento_a = str_a[len(str_a) - len(str_b):]
    return ultimo_segmento_a == str_b

a = int(input())
b = int(input())

if a >= b:
    maior, menor = a, b
    nome_maior,nome_menor = 'a', 'b'
else:
    maior,menor = b,a
    nome_maior,nome_menor = 'b', 'a'

eh_segmento = False
temp_maior = maior

while len(str(temp_maior)) >= len(str(menor)):
    if encaixa(temp_maior, menor):
        eh_segmento = True
        break
    temp_maior //= 10

if eh_segmento:
    print(f'{nome_menor} é segmento de {nome_maior}')
else:
    print('um não é segmento do outro')