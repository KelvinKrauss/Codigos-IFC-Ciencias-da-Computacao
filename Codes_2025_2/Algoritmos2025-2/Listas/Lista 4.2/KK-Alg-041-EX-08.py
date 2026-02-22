mensagem = input("Digite a mensagem: ")
deslocamento_str = input("Digite o valor do deslocamento: ")
deslocamento = int(deslocamento_str)
mensagem_codificada = ""

for char in mensagem:
    if 'a' <= char <= 'z':
        codigo = ord(char) + deslocamento
        if codigo > ord('z'):
            codigo -= 26
        elif codigo < ord('a'):
            codigo += 26
        mensagem_codificada += chr(codigo)
    elif 'A' <= char <= 'Z':
        codigo = ord(char) + deslocamento
        if codigo > ord('Z'):
            codigo -= 26
        elif codigo < ord('A'):
            codigo += 26
        mensagem_codificada += chr(codigo)
    else:
        mensagem_codificada += char
        
print("Mensagem codificada:", mensagem_codificada)