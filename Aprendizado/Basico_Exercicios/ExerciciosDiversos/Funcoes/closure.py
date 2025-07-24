def externa():
    contador = 0
    def interna():
        nonlocal contador
        for i in range(1,11):
            contador += 1
        return contador
    return interna()

print(externa())