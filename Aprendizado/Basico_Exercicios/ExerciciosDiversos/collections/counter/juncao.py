from collections import Counter as ct

lista1 = [1,2,3,4,5]
result = ct(lista1)

print(result)
lista2 = [1,1,1,12,2,2,9,9,9,9,4,1]
juncao = lista1 + lista2
print(juncao)
result = ct(juncao)
print(result)