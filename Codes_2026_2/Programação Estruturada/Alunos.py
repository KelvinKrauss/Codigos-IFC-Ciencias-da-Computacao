def confere_primo(n):
    Primo=None
    if n >= 2:
        count = 0
        for i in range(n):
            if i % n == 0:
                count =+ 1

        if count == 2:
            Primo=True

    else:
        Primo=False

    return Primo



print(confere_primo(n=int(input("Digite o numero"))))