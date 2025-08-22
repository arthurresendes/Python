lista = []

rang = range(1,100)

def retorna_par(rang):
    for n in rang:
        if n % 2 == 0:
            lista.append(n)
    return lista

print(retorna_par(rang))