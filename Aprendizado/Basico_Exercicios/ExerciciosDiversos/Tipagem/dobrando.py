def dobrando_lista(lista: list) -> list:
    dobrando = [x * 2 for x in lista]
    return list(dobrando)

print(dobrando_lista([1,2,3,4]))
print(dobrando_lista.__annotations__)