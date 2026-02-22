a = int(input("primeiro numero: "))
b = int(input("segundo numero: "))
c = int(input("terceiro numero: "))
menor = min(a, b, c)
maior = max(a, b, c)
meio = a + b + c - menor - maior
print("ordem crescente:", menor, meio, maior)