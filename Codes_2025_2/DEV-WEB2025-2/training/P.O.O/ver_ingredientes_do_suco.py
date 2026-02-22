class Ingredientes_suco:
    def __init__(self, açucar, suavidade):
        self.açucar = açucar
        self.suavidade = suavidade
    def detalhes(self):
        acerola, uva, morango = False, False, False
        if self.açucar <= 50 and self.suavidade == "S" or self.suavidade == "A":
            acerola = True
        elif 50 < self.açucar <= 99 and self.suavidade == "S":
            uva = True
        else:
            morango = True
        return acerola, uva, morango
            
suco1 = Ingredientes_suco(int(input("Digite em gramas a quantidade de açucar :")),str(input("Digite a suavidade :/S/ para suave/A/ para amargo/D/ para doce")))

a, b, c = (suco1.detalhes())
if a == True:
    print("o suco é de Acerola")
elif b == True:
    print("o suco é de Uva")
elif c == True:
    print("O suco é de Morango")
else:
    print("não sabemos")