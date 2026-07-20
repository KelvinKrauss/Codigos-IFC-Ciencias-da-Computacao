from NoLista import NoLista

class Pilha:
    def __init__(self):
        self.topo = None

    def push(self, v):
        novo = NoLista(v)
        novo.prox = self.topo
        self.topo = novo

    def vazia(self):
        return self.topo is None

    def pop(self):
        if self.vazia(): 
            raise Exception("Erro: A pilha está vazia")
        
        valor = self.topo.info
        self.topo = self.topo.prox
        return valor

    def top(self):
        if self.vazia(): 
            raise Exception("Erro: A pilha está vazia")
        return self.topo.info

    def libera(self):
        #remove as referências para o garbage collector limpar
        self.topo = None