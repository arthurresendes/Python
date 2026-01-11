def maior_de_cada(matriz) -> list[int]:
    lista_maiores = []
    for i in matriz:
        lista_maiores.append(max(i))
    
    return lista_maiores

print(maior_de_cada([[1,2,3],[4,5,6],[7,8,9]]))