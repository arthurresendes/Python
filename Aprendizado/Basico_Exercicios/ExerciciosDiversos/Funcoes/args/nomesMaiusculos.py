def nomes_maiusculos(*names):
    lista = []
    for nome in names:
        nome  = nome.title()
        lista.append(nome)
    return lista

print(nomes_maiusculos("arthur" , 'breno' , 'fransisco'))