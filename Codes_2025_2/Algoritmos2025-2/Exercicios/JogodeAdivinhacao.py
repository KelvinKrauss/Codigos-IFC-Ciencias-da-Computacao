import random
numero = random.randrange(1,11)
meu_palpite = (int(input("adivinhe meu numero entre 1 e 10:")))
palpites= 1
                 
while meu_palpite != numero:
    palpites = palpites + 1
    meu_palpite = (int(input("adivinhe meu numero entre 1 e 10:")))
    if meu_palpite == numero:
        print("VOCE ACERTOU!")
        
print(f"voce precisou de {palpites} palpites")