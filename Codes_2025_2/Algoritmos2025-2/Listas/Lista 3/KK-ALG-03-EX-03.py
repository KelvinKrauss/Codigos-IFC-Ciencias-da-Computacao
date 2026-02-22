letra = str(input("digite uma letra do alfabeto :"))
letraminuscula = letra.lower()
if letraminuscula in['a', 'e', 'i', 'o', 'u',]:
    print(f"a letra {letra} é vogal")
else:
    print(f"a letra {letra} é consoante")