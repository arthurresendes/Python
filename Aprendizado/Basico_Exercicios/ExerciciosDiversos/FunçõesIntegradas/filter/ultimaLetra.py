nomes = ["João", "Pedro", "Lucas", "Caio", "Leo"]

def names(no):
    if no[-1] == 'o':
        return no

listagem = list(filter(names , nomes))
print(listagem)