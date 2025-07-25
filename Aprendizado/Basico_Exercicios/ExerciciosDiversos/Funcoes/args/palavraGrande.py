def palavra_grande(*palavra):
    lista = []
    for letras in palavra:
        if len(letras) > 4:
            lista.append(letras)
    tupla = tuple(lista)
    return tupla


print(palavra_grande("Arthur" , "Ola" , "Josef"))