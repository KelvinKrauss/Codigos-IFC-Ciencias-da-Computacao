def taxi(km):
    metros = km
    valor = 4
    metros = metros * 1000
    preco = (metros // 140)
    valor = valor + preco * 0.25
    return valor
   
def main(): 
    valor = taxi(float(input("Digite os kilometros percorridos :")))
    print(f"o valor é {valor} R$")

main()