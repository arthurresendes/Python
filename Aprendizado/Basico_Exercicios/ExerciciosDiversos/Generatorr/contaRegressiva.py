def conta_regressiva(n):
    while n != 0:
        yield n
        n = n - 1

gen2 = conta_regressiva(3000)
for x in gen2:
    print(x)