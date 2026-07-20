from NoListaDupla import NoListaDupla

class ListaDupla:
    def __init__(self):
        #Instancia uma nova lista vazia
        self.head = None

    def vazia(self):
        #Retorna true se a lista estiver vazia
        return self.head is None

    def insere(self, v):
        #Insere um novo nó no início da lista
        novo = NoListaDupla(v)
        novo.prox = self.head
        if self.head is not None:
            self.head.ant = novo
        self.head = novo

    def imprime(self):
        #imprime os valores armazenados na lista
        atual = self.head
        while atual is not None:
            print(atual.info)
            atual = atual.prox

    def busca(self, v):
        #Retorna a referência ao primeiro nó que contém o valor
        atual = self.head
        while atual is not None:
            if atual.info == v:
                return atual
            atual = atual.prox
        return None

    def comprimento(self):
        #Retorna o número de elementos da lista
        cont = 0
        atual = self.head
        while atual is not None:
            cont += 1
            atual = atual.prox
        return cont

    def ultimo(self):
        #Retorna a referência ao último nó
        if self.vazia():
            return None
        atual = self.head
        while atual.prox is not None:
            atual = atual.prox
        return atual

    def retira(self, v):
        #Remove o primeiro nó que contém o valor informado
        no = self.busca(v)
        if no is None:
            return

        #Se não for o primeiro da lista
        if no.ant is not None:
            no.ant.prox = no.prox
        else:
            self.head = no.prox

        #Se não for o último da lista
        if no.prox is not None:
            no.prox.ant = no.ant

    def libera(self):
        #Libera todo o conteúdo
        self.head = None

    def insereFim(self, v):
        #Insere um novo nó no final da lista
        if self.vazia():
            self.insere(v)
            return
        novo = NoListaDupla(v)
        ult = self.ultimo()
        ult.prox = novo
        novo.ant = ult

    def inserePosicao(self, v, pos):
        #inséri uma música em uma posição específica
        if pos == 1:
            self.insere(v)
            return
            
        tamanho = self.comprimento()
        if pos < 1 or pos > tamanho + 1:
            print("Erro: Posição inválida.")
            return
        
        novo = NoListaDupla(v)
        atual = self.head
        #caminha até o nó anterior à posição desejada
        for _ in range(pos - 2):
            atual = atual.prox
        
        novo.prox = atual.prox
        novo.ant = atual
        
        if atual.prox is not None:
            atual.prox.ant = novo
        atual.prox = novo

    def retiraPosicao(self, pos):
        #remover uma música a partir do valor
        if pos < 1 or pos > self.comprimento():
            print("Erro: Posição inválida.")
            return
        
        if pos == 1:
            self.head = self.head.prox
            if self.head is not None:
                self.head.ant = None
            return

        atual = self.head
        for _ in range(pos - 1):
            atual = atual.prox

        atual.ant.prox = atual.prox
        if atual.prox is not None:
            atual.prox.ant = atual.ant

    def movePosicao(self, v, nova_pos):
        #Mover uma música para outra posição
        if self.busca(v) is None:
            print("Música não encontrada.")
            return
            
        tamanho_valido = self.comprimento()
        if nova_pos < 1 or nova_pos > tamanho_valido:
            print("Erro: Posição inválida.")
            return
            
        self.retira(v)
        self.inserePosicao(v, nova_pos)

    def imprimeNumerada(self):
        #imprimi a playlist numerada
        atual = self.head
        pos = 1
        while atual is not None:
            print(f"{pos}. {atual.info}")
            atual = atual.prox
            pos += 1