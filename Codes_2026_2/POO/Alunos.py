class Node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None#aqui vai aponta pro prox nó
        
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.proximo = n2
n2.proximo=n3
atual = n1
while atual is not None:
    print(atual.dado)
    atual = atual.proximo