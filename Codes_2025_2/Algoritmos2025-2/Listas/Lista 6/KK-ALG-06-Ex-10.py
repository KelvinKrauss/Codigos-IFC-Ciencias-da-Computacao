def Formatando_uma_lista(lista):
    if len(lista) == 2:
        frutas = " e ".join(lista)
        return frutas
    elif len(lista) == 1:
        frutas = "".join(lista)
        return frutas
    elif len(lista) >= 3:
        frutas = ", ".join(lista[0:len(lista) - 1])
        ultima_fruta = lista[len(lista) -1]
        return frutas + " e " + ultima_fruta

def main():
    lista = ['maçãs','bananas','morangos','uvas']
    frutas = Formatando_uma_lista(lista)
    print(frutas)

main()