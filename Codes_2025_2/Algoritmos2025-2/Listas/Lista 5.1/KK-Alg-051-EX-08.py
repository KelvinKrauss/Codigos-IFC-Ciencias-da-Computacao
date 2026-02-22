def cd(n):
    text = str(n)
    return len(text)
    
n = int(input("Digite o número :"))
dig = cd(n)
print(f"O numero de dígitos é {dig}")