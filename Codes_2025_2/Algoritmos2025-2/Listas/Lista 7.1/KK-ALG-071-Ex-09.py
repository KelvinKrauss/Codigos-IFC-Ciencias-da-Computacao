def media_notas(dados):
    notas = dados.values()
    return sum(notas) / len(notas)
def acima_da_media(dados):
    media = media_notas(dados)
    notas = dados.values()
    notas_acima = []
    for nome,nota in dados.items():
        if nota > media:
            notas_acima.append(nome)
    return notas_acima
    

def main():
    alunos = {
        "Pedro" : 6.0,
        "Julia" : 4.0,
        "Jose" : 3.2,
        "Joao" : 8.9,
    }
    
    print(f"a media é: {media_notas(alunos)}")
    print(f"os alunos acima da média são: {acima_da_media(alunos)}")
    
main()