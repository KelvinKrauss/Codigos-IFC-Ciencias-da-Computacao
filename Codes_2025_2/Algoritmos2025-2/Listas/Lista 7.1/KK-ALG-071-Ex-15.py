def mesclar_dicts(d1,d2):
    d3 = {}
    for key in d1:
        d3[key] = d1[key]
    for key in d2:
        d3[key] = d2[key]
    return d3
print(mesclar_dicts({"joao": 18, "ana": 18}, {"pedro" : 22, "Bernardo" : 23,"joao":19}))