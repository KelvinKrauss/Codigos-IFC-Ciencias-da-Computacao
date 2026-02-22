def preco_envio_e_commerce(itens):
    if itens >= 1:
        preco = 10.95
        for _ in range(itens):
            preco = preco + 2.95
        return preco - 2.95
    else:
        return 0.00

def main():
    preco = preco_envio_e_commerce(int(input("Digite a quantidade de itens : ")))
    print(f"O custo de envio é {preco:.2f} R$")
    
main()