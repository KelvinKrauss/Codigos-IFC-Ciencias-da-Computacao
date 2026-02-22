nota = str(input("digite a nota no formato (letra)/(numero) :"))
notaminuscula = nota.lower()
letra = str(notaminuscula[0])
oitava = int(notaminuscula[1])
if oitava > 8 or letra not in ['a','b','c','d','e','g','f']:
    print("as oitavas vão somente até 8 e as letras são a, b, c, d, e, f, g")
elif letra == "c":
    frequenciabase = 261.63
    Frequencia = frequenciabase / 2 ** (4 - (oitava))
    print (Frequencia)
elif letra == "d":
    frequenciabase = 293.66
    Frequencia = frequenciabase / 2 ** (4 - (oitava))
    print (Frequencia)
elif letra == "e":
    frequenciabase = 329.63
    Frequencia = frequenciabase / 2 ** (4 - (oitava))
    print (Frequencia)
elif letra == "f":
    frequenciabase = 349.23
    frequencia = frequenciabase / 2 ** (4 - (oitava))
    print (frequencia)
elif letra == "g":
    frequenciabase = 392.00
    frequencia = frequenciabase / 2 ** (4 - (oitava))
    print (frequencia)
elif letra == "a":
    frequenciabase = 440.00
    frequencia = frequenciabase / 2 ** (4 - (oitava))
elif letra == "b":
    frequenciabase = 493.88
    frequencia = frequenciabase / 2 ** (4 - (oitava))