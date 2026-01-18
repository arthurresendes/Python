"""
Collections é conhecido por grande performace em tipo de dados de container. Listas são exemplos de containers.

Counter é uma coleção que conta os elementos de um iteravel,como uma lista ou tupla e retorna um dicionario com os elementos como chaves e suas contagens como valores 

as significa que esta chamando a classe Counter do modulo collections e renomeando para Ct


"""

from collections import Counter as Ct

lista1 = ['a', 'b', 'a', 'c', 'b', 'a']

contagem = Ct(lista1)

print("Retorna um dicionario com os elementos e a quantidade de elementos em tal iteravel")

print(contagem)
print(type(contagem))
print(Ct("Arthur Resende")) 

texto = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

print("Com o split , podemos tornar mais dinamico e fazer contar quantas palavras em um textp ele aparece")
lista2 = texto.split()
print(lista2)
resultado = Ct(lista2)
print(resultado)

print("\n")

print("Conseguimos com o ,most_common(numero que quer que apareca) pegar os mais comuns de um iteravel")
print(resultado.most_common(3))