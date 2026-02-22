def consultar_idade(nome, idades):
    return idades.get(nome)

n = "Pedro"
idades = {
    "Pedro" : 17,
    "João" : 18,
}
print(consultar_idade(n,idades))
    