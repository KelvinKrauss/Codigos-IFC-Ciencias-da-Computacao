def Busca_Divisor(n):
    divisores = []
    divisor = 0
    for _ in range (n):
        divisor = divisor + 1
        if n % divisor == 0 and divisor < n:
            divisor_str = str(divisor)
            divisores.append(divisor_str)
        else:
            continue
    return divisores

def main():
    n = int(input("Digite o número : "))
    divisores = Busca_Divisor(n)
    print(f"O número {n} é divisivel por : ")
    print(",".join(divisores))
    
main()