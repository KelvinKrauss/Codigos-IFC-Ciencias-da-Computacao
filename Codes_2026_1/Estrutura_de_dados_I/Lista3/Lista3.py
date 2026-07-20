class NoLista:
    def __init__(self, info):
        self.__info = info
        self.__prox = None

    def set_info(self, info): self.__info = info
    def get_info(self): return self.__info
    def set_prox(self, prox): self.__prox = prox
    def get_prox(self): return self.__prox

class Lista:
    def __init__(self):
        self.__prim = None

    def get_prim(self): return self.__prim

    def vazia(self): return self.__prim is None

    def insere(self, v):
        novo = NoLista(v)
        novo.set_prox(self.__prim)
        self.__prim = novo

    def imprime(self):
        atual = self.__prim
        while atual:
            print(atual.get_info(), end=" -> ")
            atual = atual.get_prox()
        print("None")

    def busca(self, v):
        atual = self.__prim
        while atual:
            if atual.get_info() == v: return atual
            atual = atual.get_prox()
        return None

    def comprimento(self):
        c, atual = 0, self.__prim
        while atual:
            c += 1
            atual = atual.get_prox()
        return c

    def ultimo(self):
        if self.vazia(): return None
        atual = self.__prim
        while atual.get_prox():
            atual = atual.get_prox()
        return atual

    def retira(self, v):
        ant, atual = None, self.__prim
        while atual and atual.get_info() != v:
            ant, atual = atual, aktual.get_prox()
        if not atual: return
        if not ant: self.__prim = atual.get_prox()
        else: ant.set_prox(atual.get_prox())

    def libera(self): self.__prim = None

    def insereFim(self, v):
        if self.vazia(): self.insere(v)
        else: self.ultimo().set_prox(NoLista(v))

    def igual(self, l):
        p1, p2 = self.__prim, l.get_prim()
        while p1 and p2:
            if p1.get_info() != p2.get_info(): return False
            p1, p2 = p1.get_prox(), p2.get_prox()
        return p1 is None and p2 is None

    def imprimeRecursivo(self):
        self.__imprimeRecAux(self.__prim)
        print("None")

    def __imprimeRecAux(self, n):
        if n:
            print(n.get_info(), end=" -> ")
            self.__imprimeRecAux(n.get_prox())

    def retiraRecursivo(self, v):
        self.__prim = self.__retiraRecAux(self.__prim, v)

    def __retiraRecAux(self, n, v):
        if not n: return None
        if n.get_info() == v: return n.get_prox()
        n.set_prox(self.__retiraRecAux(n.get_prox(), v))
        return n

    def igualRecursivo(self, l):
        return self.__igualRecAux(self.__prim, l.get_prim())

    def __igualRecAux(self, n1, n2):
        if not n1 and not n2: return True
        if not n1 or not n2 or n1.get_info() != n2.get_info(): return False
        return self.__igualRecAux(n1.get_prox(), n2.get_prox())

    def comprimentoRecursivo(self):
        return self.__compRecAux(self.__prim)

    def __compRecAux(self, n):
        return 0 if not n else 1 + self.__compRecAux(n.get_prox())

class ListaMain:
    def main():
        l1 = Lista()
        l1.insere(10)
        l1.insereFim(20)
        l1.imprimeRecursivo()
        
        l2 = Lista()
        l2.insere(10)
        l2.insereFim(20)
        
        print("Iguais:", l1.igualRecursivo(l2))
        l1.retiraRecursivo(10)
        l1.imprime()

if __name__ == "__main__":
    ListaMain.main()