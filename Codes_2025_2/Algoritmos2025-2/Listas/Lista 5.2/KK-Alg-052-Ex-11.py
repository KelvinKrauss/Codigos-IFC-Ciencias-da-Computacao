def senha_aleatoria():
    import random
    comprimento = random.randint(7,10)
    senha = []
    for _ in range (comprimento):
        n = random.randint(33,126)
        senha.append(chr(n))
    senha_organizada = "".join(senha)
    return senha_organizada

def main():
    print(senha_aleatoria())
    
main()