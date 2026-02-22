import random
total = 100
numero = random.randrange(1,101)
meu_palpite = (int(input("adivinhe meu numero entre 1 e 100:")))
palpites = 1
if meu_palpite < numero:
    print("é maior")
if meu_palpite > numero:
    print("é menor")
                 
while meu_palpite != numero:
    palpites = palpites + 1
    meu_palpite = (int(input("adivinhe meu numero entre 1 e 100:")))
    if meu_palpite < numero:
        print("é maior")
    elif meu_palpite > numero:
        print("é menor")
    elif meu_palpite == numero:
        print("VOCE ACERTOU!")
        
print(f"voce precisou de {palpites} palpites")