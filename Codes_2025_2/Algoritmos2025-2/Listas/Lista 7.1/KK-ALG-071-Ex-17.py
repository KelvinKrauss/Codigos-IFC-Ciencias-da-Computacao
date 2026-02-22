def amigos_em_comun(pessoa1, pessoa2, rede_de_amigos):
    if pessoa1 in rede_de_amigos and pessoa2 in rede_de_amigos:
        amigos_p1 = rede_de_amigos[pessoa1]
        amigos_p2 = rede_de_amigos[pessoa2]
        return amigos_p1 & amigos_p2
    else:
        return "Pessoa não encontrada"

rede_de_amigos = {
    "Pedro" : {"Jõao","Maria"},
    "Jõao" : {"Pedro","Júlio"},
    "Maria" : {"Pedro"},
    "júlio" : {"Jõao", "Maria"}
}

pessoa1,pessoa2 = "Maria","Jõao"
print(amigos_em_comun(pessoa1,pessoa2,rede_de_amigos))