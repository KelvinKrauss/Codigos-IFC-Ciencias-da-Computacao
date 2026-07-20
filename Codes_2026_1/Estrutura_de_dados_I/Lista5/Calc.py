from Pilha import Pilha

class Calc:
    def __init__(self):
        self.p = Pilha()
        self.formato = "{:.2f}"

    def operando(self, v):
        self.p.push(v)
        print(self.formato.format(self.p.top()))

    def operador(self, op):
        b = 0.0
        if not self.p.vazia():
            b = self.p.pop()
            
        a = 0.0
        if not self.p.vazia():
            a = self.p.pop()
        
        #faz a conta dependendo do operador
        if op == '+': 
            res = a + b
        elif op == '-': 
            res = a - b
        elif op == '*': 
            res = a * b
        elif op == '/':
            if b == 0:
                print("Erro: Divisão por zero")
                return
            res = a / b
            
        self.operando(res)

    def libera(self):
        self.p.libera()