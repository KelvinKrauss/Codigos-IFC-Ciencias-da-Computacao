class node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo=None
        self.anterior= None
                
class ListaEncadeada:
    def __init__(self):
        self.head=None
    def adicionar_no(self, dado):
        
        novo_no = node(dado)
        
        if self.head is None:
            self.head = novo_no
            return
        
        ultimo_no = self.head
        
        while ultimo_no.proximo:
            ultimo_no = ultimo_no.proximo
            
        ultimo_no.proximo = novo_no
    def exibir(self):
        no_atual = self.head
        while no_atual:
            print(no_atual.dado, end=" -> ")
            no_atual=no_atual.proximo
        print("None")
    
minha_lista = ListaEncadeada()

minha_lista.adicionar_no(10)
minha_lista.adicionar_no(20)
minha_lista.adicionar_no(30)
print("conteudo da lista")
minha_lista.exibir()
