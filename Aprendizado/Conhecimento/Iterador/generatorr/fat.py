def numero_fatorial(num):
    fat = 1
    contador = 1
    while contador < num + 1:
        fat = fat * contador
        yield fat
        contador += 1

fatorial = numero_fatorial(5)

for n in fatorial:
    print(n)