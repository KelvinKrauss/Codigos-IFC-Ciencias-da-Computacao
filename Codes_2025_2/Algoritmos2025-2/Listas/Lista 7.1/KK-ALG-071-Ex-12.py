def inverter_dict(d):
    dic_inv = {}
    for key, value in d.items():
        dic_inv[value] = key
    return dic_inv
    

d = {
    "branco" : "amarelo",
    "preto" : "branco",
    "azul" : "lilás",
}

print(inverter_dict(d))