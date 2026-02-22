def imprime_nome(nome):
    frase = str(input("digite a frase :"))
    for _ in range (5):
        print(frase,nome)

imprime_nome(str(input("Digite o nome")))