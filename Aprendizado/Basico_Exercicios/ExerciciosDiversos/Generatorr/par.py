def pares(num):
    contador = 0
    while contador < num:
        if contador % 2 == 0:
            yield contador
        contador += 1

gen = pares(2000)

for x in gen:
    print(x)