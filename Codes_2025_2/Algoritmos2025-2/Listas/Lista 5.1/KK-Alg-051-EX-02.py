def imprime_n_vezes(nome, n):
    for i in range (n):
        print(f"{nome + " "}{n} vezes")

n = int(input("Digite a quantidade de vezes"))
nome = str(input("Digite a frase a ser repetida :"))
imprime_n_vezes(nome, n)