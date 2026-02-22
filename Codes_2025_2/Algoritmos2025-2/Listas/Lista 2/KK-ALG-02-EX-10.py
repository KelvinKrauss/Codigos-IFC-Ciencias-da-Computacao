matricula = input("Digite o numero da matricula (AASDDD): ")
ano = matricula[0:2]
print(f"Ano da matricula: 20{ano}")
semestre_t = matricula[2]
semestre_n = int(semestre_t)
if semestre_n == 1:
    print("Semestre: Primeiro Semestre")
else:
    print("Semestre: Segundo Semestre")