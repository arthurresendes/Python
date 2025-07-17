"""
Listas em Python funciona como vetores/matrizes(arrays) em outras linguagens com a diferena de serem DINÂMICO e tambem podemos colocar QUALQUER tipo de dado

Em python não tem tamanho fixo igual em C ou em Java , podemos criar a lista e simplesmente ir adicionando os itens

As listas em python são representadas por []
variavel.sort()
novaVariavel  = sorted(antigaVariavel)

len(lista)      # retorna o tamanho da lista
max(lista)      # retorna o maior valor
min(lista)      # retorna o menor valor
sum(lista)      # retorna a soma dos valores
sorted(lista)   # retorna uma nova lista ordenada

lista.append(4)      # adiciona um item
lista.pop()          # remove o último item
lista.sort()         # ordena a lista
lista.reverse()      # inverte a lista
lista.clear()        # limpa a lista
lista.count(3)       # conta quantas vezes o 3 aparece
lista.index()        # Retorna a posição do elemento
"""
estiloLista = type([])
print(estiloLista)

lista1 = [1 , 99 , 4, 15 , 22 , 3 , 1 , 44 , 42, 27]

lista2 = ['a' , 'r' , 't' , 'h' , 'u' , 'r' 'r', 'e' ,'s', 'e' ,'n' , 'd', 'e']

lista3 = list(range(11))

lista4 = []

lista5 = list("Arthur Resende")

if 8 in lista3:
    print("O número 8 está na lista3")
else:
    print("Nao foi encontradao!!")

#Ordenando a lista
print(lista1)
lista1.sort()
print("--Ordenando a lista--")
print(lista1)

#Caso o usuario digite uma lista e preencha os valores tem outro metodo de ordenação
print("\n")
print("Ordenando com sorted")
for i in range(5):
    valor = int(input("Digite o valor: "))
    lista4.append(valor)

listaOrdenada = sorted(lista4)

for i in listaOrdenada:
    print(i, end= ' ')

# Contando itens em uma lista
print("\n")
print("Contando itens em uma lista")
print(lista5.count('r') + lista5.count('R'))

# Com o .append() podemos adicionar novos itens na lista
print('\n')
lista1.append(5)
lista1.sort()
print("Adicionamos o valor 5 na lista1 e ordenamos com o .sort()")
print(lista1)

# So da para adicionar varios valores ao append se fizer dessa forma:
#lista1.append([6,220,100])

# Podemos adicionar varios valores na lista com o . extend()
print('\n')
lista1.extend([300,400,500])
print(lista1)

#Podemos adicionar um valor em posição especifica com o .insert()
print('\n')
print("Adicionando o  'A' na posição 0 com o insert que é utilizado para colocar um valor na posição que quiser")
lista2.insert(0, 'A')
print(lista2)

# Podemos remover um valor com o remove()


#Podemos juntar duas listas com +
print("Junção de lista com +")
lista6 = lista1 + lista2
print(lista6)

# Podemos reverter uma lista com o .reverse() ou com [:: -1]
print("\n")
print("Revertetndo lista com .reverse()")
lista1.reverse() # or [:: -1]
print(lista1)

# Podemos copiar uma lista com o .copy()
print("\n")
print("Copiando lista em outra lista com o .copy()")
lista7 = lista1.copy()
lista7.sort()
print(lista7)

# Podemos achar a quantidade de itens com o len()
print("\n")
print("Quantidade de itens na lista 1: ")
print(len(lista1))

# Podemos achar o maior e o menos valor com max() e min()
print("\n")
print("Soma dos valores da lista1: ")
print(sum(lista1))

print("Maior valor: ")
print(max(lista1))

print("Menor valor: ")
print(min(lista1))

print("Tamanho da lista1: ")
print(len(lista1)) 

# Podemos remover o ultimo item com o .pop()
print("\n")
lista1.sort()
lista1.pop()
print("Removendo o ultimo elemento com o .pop()")
print(lista1)
lista1.pop(0)
print("\n")
print("Podemos tambem remover um indice especifico passando o valor dentro do .pop() , ex: .pop(0)")
print(lista1)

# Podemos limpar a lista com o .clear()
print("\n")
print("Lista 7 antes do clear: ")
print(lista7)
lista7.clear()
print("Lista7 foi limpa com o .clear()")
print(lista7)

# Podemos transformar uma string em uma lista com o .split() , o espaço conta como virgula na transformação , ao menos se você definir dentro do () qual é o seu separador
print("\n")
print("Transformando string em lista com .split()")
nome = "Arthur Resende , Pythonista"
print(nome)
nome = nome.split(",")
print(nome) 

# Converter uma lista em string com o .join(), podemos colocar o que quisermos entre os valores
nomeString = "$".join(nome)
print(nomeString)

print("Podemos mesclar diferentes tipos de variaveis em uma lista")
listaMesclada = [1 , 3 ,6 , True , 'Ola' , '4', [1,2,3] , 444777]
print(listaMesclada)
print(type(listaMesclada)) 

# Iterando uma lista , utilizando o for
print("\n")
soma = 0
print("Iterando uma lista: ")

for elemento in lista1:
    print(elemento , end=" ")
    soma = soma + elemento

print(f"\nA soma dos elementos da lista1 eh: {soma}") 

# Iterando uma lista com o while
print("\n")
carrinho = []
produto = ""

while produto != "sair":
    produto = input("Digite o nome do produto ou 'sair': ").lower()
    if produto != "sair":
        carrinho.append(produto)

for produto in carrinho:
    print(produto, end = " ")

# Fazemos acessos ao elementos de forma indexada
print("\n")
print("Acessando elementos de uma lista: ")

cores = ['azul', 'verde' ,'vermelho','branco', 'preto' , 'azul']

print(cores[-1] , cores.index('preto')) # Acessa o ultimo elemento

print(cores[0] , cores.index('azul')) #Acessa o primeiro elemento azul

print(cores[0] , cores.index('azul' , 1)) #Acessa o elemento azul a partir do indice 1

# Podemos iterar uma lista com enumarate() que retorna o indice e o nome da cor
for indice , cor in enumerate(cores):
    print(indice , cor)
"""

for cor in cores:
    print(cor, end = " ")

indice = 0

while indice < len(cores):
    print(cores[indice] , end = " ")
    indice += 1

"""
lista8 = [1,2,3,4,]

print("\nAcessando toda a lista")

print(lista8[::])

print("Acessando a lista apartir do primeiro elemento")

print(lista8[1:])

print("Acessando os dois primeiros elemento da lista")

print(lista8[:2])

print("Começa acessando o primeiro elemento da lista e vai indo de dois em dois")

print(lista8[1::2])

print("Invertendo a lista")

print(lista8[:: -1])

# Transforma uma lista em uma tupla
print("\nTransformando uma lista em tupla")

lista9 = [1,2,3,4,5,6]

print("Lista: ")

print(lista9)

print(type(lista9))


tupla1 = tuple(lista9)

print("Tupla: ")

print(tupla1)

print(type(tupla1)) 

#Copiando uma lista para a outra com shallow copy e deep copy , no deep copy uma lista dentro da outra é copiada , enquanto no shallow copy não sendo apenas referenciada
