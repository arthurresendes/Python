def segundo_maior(lista: list[int]) -> int:
    lista.remove(max(lista))
    return max(lista)

print(segundo_maior([1,2,3,4,5,6,7,8,9]))