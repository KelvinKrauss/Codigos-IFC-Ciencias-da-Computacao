class carros:
    def __init__(self, modelo, ano, velocidade):
        self.velocidade = velocidade
        self.modelo = modelo
        self.ano = ano
    def detalhes(self):
        return f"O carro {self.modelo} é ano :{self.ano} e alcança a velocidade de {self.velocidade}"
    
carro1 = carros(str(input("Digite a marca")),int(input("Digite o ano")),int(input("Digite a velocidade")))
print(carro1.detalhes())
velocidadeint = int(carro1.velocidade)
if velocidadeint >= 90:
    print("é rapido") 