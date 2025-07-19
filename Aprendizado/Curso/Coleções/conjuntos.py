"""
Conjuntos  em qualquer linguagem estamos fazendo referencia a teoria dos conjuntos da matematica

Conjuntos em py são chamados de set(), sem possuir valores duplicados e não são ordenados

"""

# Definido um conjunto

# Forma 1
s = set({1,2,3,4,5,6,7,2,2,3})
print(type(s))
print(s)

# Forma 2: mais comum
s2 = {1,2,3,4,5,6,7,1,2,3,4}
print(type(s2))
print(s2)

if 3 in s2:
    print("Tem o valor 3 no conjunto")
else: 
    print("Não tem o valor 3")

s3 = {1,'a', True, 34.22}
for valor in s3:
    print(valor)


# Usos interessantes com o set()

cidades = ['bela horizonte' , 'sao paulo' , 'campo grande' , 'cuiaba' , 'campo grande' , 'sao paulo' , 'cuiaba']
print(cidades)
print("Total cidades: ")
print(len(cidades))

cidadeConjunto = set(cidades)
print("Quantidade de cidades sem repetição: ")
print(cidadeConjunto)
print(len(cidadeConjunto))


# Conjuntos sao mutaveis , duplicidade não gera erro , porem não aparece
s4 = {1,2,3}
#Adição
s4.add(4)
print(s4)
# Remoção
s4.remove(4)
print(s4)
