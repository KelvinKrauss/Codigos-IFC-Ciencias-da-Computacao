from Fila import Fila

class FilaVetor(Fila):
    def __init__(self, tam):
        self.tam = tam
        self.n = 0
        self.ini = 0
        self.vet = [0] * tam

    def isEmpty(self):
        return self.n == 0

    def enqueue(self, v):
        if self.n == self.tam:
            raise Exception("Fila cheia")
        pos = (self.ini + self.n) % self.tam
        self.vet[pos] = v
        self.n += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Fila vazia")
        v = self.vet[self.ini]
        self.ini = (self.ini + 1) % self.tam
        self.n -= 1
        return v

    def reset(self):
        self.n = 0
        self.ini = 0

    def __str__(self):
        s = ""
        for i in range(self.n):
            idx = (self.ini + i) % self.tam
            s += str(self.vet[idx]) + " "
        return s.strip()

    def concatena(self, f2):
        f3 = FilaVetor(self.tam + f2.tam)
        for i in range(self.n):
            f3.enqueue(self.vet[(self.ini + i) % self.tam])
        for i in range(f2.n):
            f3.enqueue(f2.vet[(f2.ini + i) % f2.tam])
        return f3

    def merge(self, f2):
        f3 = FilaVetor(self.tam + f2.tam)
        limite = self.n if self.n > f2.n else f2.n
        for i in range(limite):
            if i < self.n:
                f3.enqueue(self.vet[(self.ini + i) % self.tam])
            if i < f2.n:
                f3.enqueue(f2.vet[(f2.ini + i) % f2.tam])
        return f3