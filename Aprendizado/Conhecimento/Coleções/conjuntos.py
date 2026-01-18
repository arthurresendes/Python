"""
Conjuntos  em qualquer linguagem estamos fazendo referencia a teoria dos conjuntos da matematica

Conjuntos em py são chamados de set(), sem possuir valores duplicados e não são ordenados

Conjunto não são indexados
"""

# Definido um conjunto

# Forma 1
s = set({1,2,3,4,5,6,7,2,2,3})
print(max(s))
print(min(s))
print(sum(s))
print(len(s))
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
# Forma 1
s4.remove(4)
# Forma 2
s4.add(5)
s4.discard(5)
print(s4)

# Copiando um set para o outro
#Shallow - tudo muda
s6 = {1,2,3,4}
print(s6)
novo = s6
novo.add(5)
print(novo,s6)
# Deep - so muda o novo
new = s6.copy()
new.add(6)
print(new,s6)

# Limpando o conjunto
s6.clear()
print(s6)

# Conjunto metodos matematicos
estudantesPy = {'Arthur' , 'Jose', 'Pedro' , 'Maria', 'Escobar', 'Lalo'}
estudantesJava = {'Arthur' , 'Jose', 'Carlos' , 'Davi', 'Tuco'}

# Utilizando o union 
unicos1 = estudantesPy.union(estudantesJava)
print(unicos1)

# Utilizando o pipe |
unicos2 = estudantesPy | estudantesJava
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambas as linguagens
ambos = estudantesPy.intersection(estudantesJava)

# Outra forma
ambos2 = estudantesPy & estudantesJava
print(ambos2)

# Gera um conjunto de estudantes que estao em apenas um curso

soPy = estudantesPy.difference(estudantesJava)
soJava = estudantesJava.difference(estudantesPy)


