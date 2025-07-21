"""

Em Python, OrderedDict é uma subclasse de dict que lembra a ordem em que as chaves foram inseridas. Diferentemente dos dicionários regulares (que não garantem uma ordem específica), o OrderedDict mantém a ordem de inserção, permitindo iterar sobre os itens na mesma ordem em que foram adicionados. Essa funcionalidade é útil principalmente em versões do Python anteriores à 3.7, onde os dicionários regulares não preservavam a ordem.

"""
from collections import OrderedDict as od
# Ordem não eh garantida
dicionario = {'a':1, 'b':2, "c": 3}
print(dicionario)

for chave , valor in dicionario.items():
    print(chave,valor)

# Aqui temos a ordem garantida

dicionario2 = od({'a':1, 'b':2, "c": 3})
chave = input("Digite uma chave: ")
valor = input("Digite o seu valor: ")
dicionario2[chave] = valor

for chave , valor in dicionario2.items():
    print(chave,valor)

print("Dicionario comum a ordem não é garantida: ")
dict1 = {'a':1, 'b':2}
dict2 = {'b':2, 'a':1}
print(dict1 == dict2)

print("Ja no ordereDict a ordem é garantida: ")
odict1 = od({'a':1, 'b':2})
odict2 = od({'b':2, 'a':1})
print(odict1 == odict2)