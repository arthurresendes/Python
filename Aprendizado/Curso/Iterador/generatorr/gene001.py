'''
Utiliza yield , pode utilizar varios yield, retorna um generator

O yield ele retorna o numero todas vezes ate o fim do while , esperando o proximo next

'''

def conta_ate(valor):
    contador = 1
    while contador <= valor:
        yield contador # Retorna o contador
        contador += 1

gen = conta_ate(5)
gen2 = list(conta_ate(10))

for num in gen:
    print(num)


# Com lista
print(gen2)