def Confere_se_é_perfeito(n):
    divisor = 0
    divisores = []
    for _ in range(n):
        divisor = divisor + 1
        if n % divisor == 0 and divisor < n:
            divisores.append(divisor)
    if sum(divisores) == n:
        return True
    else:
        return False

def main():
    n = 0
    numeros_perfeitos = []
    for _ in range (10000):
        n = n + 1
        n_str = str(n)
        numero_perfeito = Confere_se_é_perfeito(n)
        if numero_perfeito == True:
            numeros_perfeitos.append(n_str)
    print(",".join(numeros_perfeitos))
    
main()