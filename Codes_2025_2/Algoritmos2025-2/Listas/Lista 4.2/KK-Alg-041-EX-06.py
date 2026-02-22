while True:
    bits_str = input("Digite 8 bits (linha em branco para sair): ")
    
    if bits_str == "":
        break
    
    if len(bits_str) != 8 or not all(c in '01' for c in bits_str):
        print("Erro: por favor, digite uma sequência de 8 bits (0s e 1s).")
        continue

    contagem_de_uns = bits_str.count('1')
    
    if contagem_de_uns % 2 == 0:
        print("O bit de paridade deve ser 0.")
    else:
        print("O bit de paridade deve ser 1.")