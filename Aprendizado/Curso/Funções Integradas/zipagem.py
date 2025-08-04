"""
Zip -> Cria um iteravel chamado zip object que agrega elementos de cada um dos iteraveis passados como entreada em pares


"""

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [10,9,5,6,4]

zip1 = zip(lista1,lista2)

print(list(zip1))

nomes = ['Arthur' , 'Maria' , 'Jose']
idade = [18, 15, 17]
sonho = ['Programador' , 'Manicure', 'Heroi']

zipagem = zip(nomes,idade,sonho)

print(list(zipagem))

print(dict(zipagem))

zipagem2 = list(zip(lista1,lista2,lista3))

print(zipagem2) 

tupla = 1,2,3

dicionario = {'a': 4,"b": 5, 'c': 6}

zipagem4 = list(zip(tupla,dicionario.keys(),lista3))

print(zipagem4)

dados = [(10,2),(10,2),(10,2),(10,2),(10,2)]

print(list(zip(*dados)))

prova1 = [80,91,78]
prova2 = [98,89,53]
alunos = ['maria','pedro','carla']

final = {dado[0]:max(dado[1],dado[2]) for dado in zip(alunos,prova1,prova2)}

print(final)

final2 = zip(alunos, map(lambda nota: max(nota) , zip(prova1,prova2)))

print(dict(final2))