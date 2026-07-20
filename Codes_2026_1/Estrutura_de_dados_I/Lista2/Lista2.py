class NoLista:
    # Construtor e métodos acessores para o nó
    def __init__(self, info):
        self.__info = info
        self.__prox = None

    def set_info(self, info):
        self.__info = info

    def get_info(self):
        return self.__info

    def set_prox(self, prox):
        self.__prox = prox

    def get_prox(self):
        return self.__prox

    def __str__(self):
        return str(self.__info)

class Lista:
    # Inicializa uma lista vazia
    def __init__(self):
        self.__prim = None

    # Insere um novo nó no início da lista
    def insere(self, v):
        novo = NoLista(v)
        novo.set_prox(self.__prim)
        self.__prim = novo

    # Imprime os valores armazenados
    def imprime(self):
        atual = self.__prim
        while atual is not None:
            print(atual.get_info(), end=" -> ")
            atual = atual.get_prox()
        print("None")

    # Retorna a representação em string da lista (equivalente ao toString)
    def __str__(self):
        resultado = ""
        atual = self.__prim
        while atual is not None:
            resultado += str(atual.get_info()) + " -> "
            atual = atual.get_prox()
        resultado += "None"
        return resultado

    # Informa se a lista está vazia
    def vazia(self):
        return self.__prim is None

    # Retorna o endereço do primeiro nó com o valor v, ou None
    def busca(self, v):
        atual = self.__prim
        while atual is not None:
            if atual.get_info() == v:
                return atual
            atual = atual.get_prox()
        return None

    # Calcula e retorna o número atual de elementos
    def comprimento(self):
        cont = 0
        atual = self.__prim
        while atual is not None:
            cont += 1
            atual = atual.get_prox()
        return cont

    # Retorna o endereço do último nó da lista, ou None se vazia
    def ultimo(self):
        if self.vazia():
            return None
        atual = self.__prim
        while atual.get_prox() is not None:
            atual = atual.get_prox()
        return atual

    # Remove o primeiro nó que contiver o valor v
    def retira(self, v):
        anterior = None
        atual = self.__prim

        while atual is not None and atual.get_info() != v:
            anterior = atual
            atual = atual.get_prox()

        # Se não encontrou o valor, não faz nada
        if atual is None:
            return

        # Se for o primeiro elemento
        if anterior is None:
            self.__prim = atual.get_prox()
        else:
            anterior.set_prox(atual.get_prox())

    # Destrói toda a lista
    def libera(self):
        # No Python, o Garbage Collector limpa a memória automaticamente 
        # quando perdemos a referência aos objetos.
        self.__prim = None


# Programa main
if __name__ == "__main__":
    lista = Lista()
    
    print("Testando lista vazia:", lista.vazia())
    
    print("\nInserindo valores 10, 20 e 30...")
    lista.insere(10)
    lista.insere(20)
    lista.insere(30)
    
    print("Lista atual (imprime)")
    lista.imprime()
    
    print("Lista atual (toString/__str__):", str(lista))
    print("Comprimento da lista:", lista.comprimento())
    
    print("\nBuscando o valor 20:", lista.busca(20))
    print("Buscando o valor 99 (não existe):", lista.busca(99))
    
    ultimo_no = lista.ultimo()
    if ultimo_no:
        print("Último elemento da lista: ", ultimo_no.get_info())
        
    print("\nRetirando o valor 20...")
    lista.retira(20)
    lista.imprime()
    print("Novo comprimento:", lista.comprimento())
    
    print("\nLiberando a lista...")
    lista.libera()
    print("Testando lista vazia após liberar:", lista.vazia())
