
def soma_lista(lista):
    assert len(lista) != 0, 'Lista não pode estar vazia'
    soma = 0
    for i in lista:
        soma += i
    # assert soma == 0, 'Lista não pode estar vazia'
    return soma

lista = [1,2,3,4,5]
lista2 = []
print(soma_lista(lista))
#print(soma_lista(lista2))