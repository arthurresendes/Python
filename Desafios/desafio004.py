lista = ['Banana','Maca','Pera','Uva','Laranja']

print (lista)


print(lista[0])

print(lista[4])


lista[2] = 'Abacaxi'

print(lista[2])


lista.remove('Maca')

del lista[2]

print(lista)


for fruta in lista:

    print('Eu gosto de' , fruta)