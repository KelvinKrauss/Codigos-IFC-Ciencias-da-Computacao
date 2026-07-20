from no_arvore_naria import NoArvoreNaria

class ArvoreNaria:
    def __init__(self):
        # construtor que instancia uma arvore vazia
        self.raiz = None

    def define_raiz(self, r):
        # define o no raiz principal da arvore
        self.raiz = r

    def insere_filho(self, pai, filho):
        # insere o no filho como filho do no pai no inicio da lista
        filho.set_prox(pai.get_prim())
        pai.set_prim(filho)

    def vazia(self):
        # retorna true se a arvore estiver vazia
        return self.raiz is None

    def pertence(self, v):
        return self._pertence_recursivo(self.raiz, v)

    def _pertence_recursivo(self, no, v):
        if no is None:
            return False
        if no.get_info() == v:
            return True
        # procura no primeiro filho ou nos proximos irmaos
        return self._pertence_recursivo(no.get_prim(), v) or self._pertence_recursivo(no.get_prox(), v)

    def num_nos(self):
        return self._num_nos_recursivo(self.raiz)

    def _num_nos_recursivo(self, no):
        if no is None:
            return 0
        return 1 + self._num_nos_recursivo(no.get_prim()) + self._num_nos_recursivo(no.get_prox())

    def folhas(self):
        return self._folhas_recursivo(self.raiz)

    def _folhas_recursivo(self, no):
        if no is None:
            return 0
        # folha nao tem filhos
        if no.get_prim() is None:
            return 1 + self._folhas_recursivo(no.get_prox())
        return self._folhas_recursivo(no.get_prim()) + self._folhas_recursivo(no.get_prox())

    def altura(self):
        return self._altura_recursivo(self.raiz)

    def _altura_recursivo(self, no):
        if no is None:
            return -1 # arvore vazia tem altura -1
        max_altura = -1
        filho = no.get_prim()
        
        while filho is not None:
            alt = self._altura_recursivo(filho)
            if alt > max_altura:
                max_altura = alt
            filho = filho.get_prox()
            
        return 1 + max_altura

    def igual(self, a):
        return self._igual_recursivo(self.raiz, a.raiz)

    def _igual_recursivo(self, n1, n2):
        if n1 is None and n2 is None:
            return True
        if n1 is None or n2 is None:
            return False
        if n1.get_info() != n2.get_info():
            return False
        return self._igual_recursivo(n1.get_prim(), n2.get_prim()) and self._igual_recursivo(n1.get_prox(), n2.get_prox())

    
    def __str__(self):
        return self._to_string_recursivo(self.raiz, "")

    def _to_string_recursivo(self, no, prefixo):
        if no is None:
            return ""
        resultado = prefixo + str(no.get_info()) + "\n"
        
        filho = no.get_prim()
        while filho is not None:
            resultado += self._to_string_recursivo(filho, prefixo + "  ")
            filho = filho.get_prox()
            
        return resultado