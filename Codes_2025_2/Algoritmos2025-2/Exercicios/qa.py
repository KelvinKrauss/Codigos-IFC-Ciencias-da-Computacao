n = int(input())
meio = n // 2

# Letra J
for i in range(n):
    linha_j_list = [' '] * n
    if i == 0:
        linha_j_list = ['#'] * n
    elif i < n - 1:
        linha_j_list[meio] = '#'
        if i == n - 2:
            linha_j_list[0] = '#'
    else: # i == n - 1
        for k in range(1, meio + 1):
            linha_j_list[k] = '#'
    print("".join(linha_j_list))