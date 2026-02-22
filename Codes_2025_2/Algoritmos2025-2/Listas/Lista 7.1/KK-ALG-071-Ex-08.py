def intersecao_multipla(lista_de_conjuntos):
    lista_interseccionada = lista_de_conjuntos
    lista_interseccionada = lista_de_conjuntos.intersection(*lista_de_conjuntos)
    return lista_interseccionada

def main():
    prox,loop,mylist,set_n = False,1,[],set()
    while True:
        while True:
            n_str = str(input(f"Digite o número para o conjunto {loop}, ou ENTER para sair : "))
            if n_str == "":
                mais_cjt = str(input("Deseja preencher mais um conjunto? S/N : "))
                if mais_cjt.lower() =="s":
                    prox = True
                elif mais_cjt.lower() == "n":
                    prox = False
                break
            else:
                n = int(n_str)
                set_n.add(n)
                print(set_n)
                mylist = set_n
                print(mylist)

            mylist = intersecao_multipla(mylist)
                
            
        if prox == False:
            break
        else:
            loop = loop + 1
            continue
            
    print (mylist)
    
main()