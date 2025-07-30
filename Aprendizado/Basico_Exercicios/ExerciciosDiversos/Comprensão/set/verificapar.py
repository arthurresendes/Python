lista = [2, 4, 4, 6, 8, 2, 10, 6]
pares_unicos = {x for x in lista if x % 2 == 0}

def multiplicaLista(listas):
    if listas > 5:
        return True
    else:
        return False

filtragem = list(filter(multiplicaLista, lista))
print(filtragem)