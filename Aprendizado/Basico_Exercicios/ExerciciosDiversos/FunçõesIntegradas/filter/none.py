dados = ["João", None, "Maria", None, "Pedro"]

def soNone(dado):
    return dado is None

listagem = list(filter(soNone , dados))
print(listagem)