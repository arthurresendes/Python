"""
Listas aninhadas

"""

# Lista aninhadas , matriz nesse exemplo
lista = [[1,2,3] , [4,5,6] , [7,8,9]]

print(lista)
# Acessando o primeiro elemento da primeira lista aninhada
print(lista[0])
print(lista[0][0])
print(lista[2])
print(lista[2][1])

# Iterando com loops:
for itens in lista:
    print(itens)
# Fazendo cada valor mostrar , pega os itens na lista , no caso pega o [1,2,3] , [4,5,6], [7,8,9] . Depois o num serve para pegar cada numeros nos itens
for itens in lista:
    for num in itens:
        print(num)

print("\n")
[[print(valor) for valor in lista]for lista in lista]

tabuleiro = [[numero for numero in range(1,4)] for valor in range(1,4)]
print(tabuleiro)

""" 
for valor in range(1,4):
    for numero in range(1,4):
"""

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1,4)] for valor in range(1,4)] 

print(velha)

print([['*' for i in range(1,4)] for j in range(1,4)])