def esta_presente(nome, presencas):
    if nome in presencas:
        return True
    else:
        return False

def presencas():
    presencas = set()
    while True:
        aluno = str(input("Digite o nome dos alunos presentes : "))
        if aluno == "":
            break
        else:
            presencas.add(aluno.lower())
            print(presencas)

    nome = str(input("Digite o nome do aluno a verificar : "))
    nome = nome.lower()
    print(esta_presente(nome, presencas))

presencas()