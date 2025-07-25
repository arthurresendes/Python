def so_string(**kwargs):
    for valor in kwargs.values():
        if not isinstance(valor,str):
            return "So vale string"
    return kwargs

print(so_string(nome='Arthur', cidade='Osasco'))

print(so_string(nome='Arthur', idade=18))