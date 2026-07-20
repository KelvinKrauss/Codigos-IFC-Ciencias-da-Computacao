class NoArvoreBinaria:
    def __init__(self, info, sae=None, sad=None):
        self.info = info
        self.sae = sae
        self.sad = sad

    def getInfo(self):
        return self.info

    def setInfo(self, info):
        self.info = info

    def getSae(self):
        return self.sae

    def setSae(self, sae):
        self.sae = sae

    def getSad(self):
        return self.sad

    def setSad(self, sad):
        self.sad = sad


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def defineRaiz(self, r):
        self.raiz = r

    def getRaiz(self):
        return self.raiz

    def vazia(self):
        return self.raiz is None

    def pertence(self, v):
        return self._pertenceRecursivo(self.raiz, v)

    def _pertenceRecursivo(self, no, v):
        if no is None:
            return False
        if no.getInfo() == v:
            return True
        return self._pertenceRecursivo(no.getSae(), v) or self._pertenceRecursivo(no.getSad(), v)

    def folhas(self):
        return self._folhasRecursivo(self.raiz)

    def _folhasRecursivo(self, no):
        if no is None:
            return 0
        if no.getSae() is None and no.getSad() is None:
            return 1
        return self._folhasRecursivo(no.getSae()) + self._folhasRecursivo(no.getSad())

    def numNos(self):
        return self._numNosRecursivo(self.raiz)

    def _numNosRecursivo(self, no):
        if no is None:
            return 0
        return 1 + self._numNosRecursivo(no.getSae()) + self._numNosRecursivo(no.getSad())

    def altura(self):
        return self._alturaRecursivo(self.raiz)

    def _alturaRecursivo(self, no):
        if no is None:
            return -1
        alturaEsquerda = self._alturaRecursivo(no.getSae())
        alturaDireita = self._alturaRecursivo(no.getSad())
        return 1 + max(alturaEsquerda, alturaDireita)

    def igual(self, a):
        if a is None:
            return False
        return self._igualRecursivo(self.raiz, a.getRaiz())

    def _igualRecursivo(self, no1, no2):
        if no1 is None and no2 is None:
            return True
        if no1 is None or no2 is None:
            return False
        if no1.getInfo() != no2.getInfo():
            return False
        return self._igualRecursivo(no1.getSae(), no2.getSae()) and self._igualRecursivo(no1.getSad(), no2.getSad())

    def imprimePre(self):
        return self._imprimePreRecursivo(self.raiz).strip()

    def _imprimePreRecursivo(self, no):
        if no is None:
            return ""
        return no.getInfo() + " " + self._imprimePreRecursivo(no.getSae()) + self._imprimePreRecursivo(no.getSad())

    def imprimeSim(self):
        return self._imprimeSimRecursivo(self.raiz).strip()

    def _imprimeSimRecursivo(self, no):
        if no is None:
            return ""
        return self._imprimeSimRecursivo(no.getSae()) + no.getInfo() + " " + self._imprimeSimRecursivo(no.getSad())

    def imprimePos(self):
        return self._imprimePosRecursivo(self.raiz).strip()

    def _imprimePosRecursivo(self, no):
        if no is None:
            return ""
        return self._imprimePosRecursivo(no.getSae()) + self._imprimePosRecursivo(no.getSad()) + no.getInfo() + " "


if __name__ == "__main__":
    brasil = NoArvoreBinaria("Brasil")
    argentina = NoArvoreBinaria("Argentina")
    franca = NoArvoreBinaria("Franca")
    alemanha = NoArvoreBinaria("Alemanha")

    semi1 = NoArvoreBinaria("Semifinal 1", brasil, argentina)
    semi2 = NoArvoreBinaria("Semifinal 2", franca, alemanha)

    final_copa = NoArvoreBinaria("Final", semi1, semi2)

    chaveamento = ArvoreBinaria()
    chaveamento.defineRaiz(final_copa)

    print(chaveamento.imprimePre())
    print(chaveamento.imprimeSim())
    print(chaveamento.imprimePos())

    print(chaveamento.numNos())
    print(chaveamento.folhas())
    print(chaveamento.altura())

    print(chaveamento.pertence("Franca"))
    print(chaveamento.pertence("Italia"))

    brasil2 = NoArvoreBinaria("Brasil")
    argentina2 = NoArvoreBinaria("Argentina")
    franca2 = NoArvoreBinaria("Franca")
    alemanha2 = NoArvoreBinaria("Alemanha")

    semi12 = NoArvoreBinaria("Semifinal 1", brasil2, argentina2)
    semi22 = NoArvoreBinaria("Semifinal 2", franca2, alemanha2)

    final_copa2 = NoArvoreBinaria("Final", semi12, semi22)

    chaveamento2 = ArvoreBinaria()
    chaveamento2.defineRaiz(final_copa2)

    print(chaveamento.igual(chaveamento2))