from ListaDupla import ListaDupla

lista = ListaDupla()

#
lista.insereFim("Eternity")
lista.insereFim("All The Flowers In Time Bends Towards The Sun")
lista.insereFim("Man of War")
lista.insereFim("come closer")

print("Playlist Original:")
lista.imprimeNumerada()

print("\nInserindo uma nova musica na posicao 2:")
lista.inserePosicao("Nova Musica", 2)
lista.imprimeNumerada()

print("\nRemovendo uma musica pelo nome:")
lista.retira("Man of War") 
lista.imprimeNumerada()

print("\nRemovendo a musica da posicao 3:")
lista.retiraPosicao(3)
lista.imprimeNumerada()

print("\nMovendo uma musica para a posicao 1:")
lista.movePosicao("come closer", 1) 
lista.imprimeNumerada()

lista.libera()