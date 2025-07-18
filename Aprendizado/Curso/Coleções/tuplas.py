"""

Tuplas (tuple) são estruturas de dados imutaveis , ou seja , são tipo uma lista só que constante.

Elas são definidas por () e não por []
Tuplas são definidas pela virgula e não pelo uso de parenteses


"""
tupla1 = (1,2,3,4,5,6)
print(tupla1)
print(type(tupla1))

#Podemos definir a tupla sem o uso de ()
tupla2 = 1,2,3,4,5,6
print(tupla2)
print(type(tupla2))

#Isso nao é uma tupla
tupla3 = (3)
print(tupla3)
print(type(tupla3))

# Isso sim eh uma tupla
tupla4 = (3,)
print(tupla4)
print(type(tupla4))

#Tupla com range
tupla5 = tuple(range(11))
print(tupla5)

#Desempacotando tupla
tupla6 = ("Arthur resende" , "Phyton")
nome , linguagem = tupla6
print(tupla6)
print(nome)
print(linguagem)

# Metodos para adição e remoção nas tuplas não existem, porem consegue fazer algumas operações se os valores forem numéricos
tupla7 = 1,2,3,4,5,6
print(sum(tupla7))
print(max(tupla7))
print(min(tupla7))
print(len(tupla7))

# Concatenação em tuplas
tuplaS = tupla1 + tupla2
print(tuplaS)

# Se quiser alterar tupla tem que fazer isso:
tupla1 = tupla1 + (7,8,9)
print(tupla1)

# Verificando se um valor está na tupla
print(1 in tupla1)
for indice , valor in enumerate(tupla1):
    print(indice , valor)

# Contando elementos em uma tupla
tupla1 = tupla1 + (1,1,1,1,1,1,1,1,1)
print(tupla1.count(1))

print("Exemplos de uso de tuplas: ")
tuplaMes = ("Janeiro" , "Fevereiro" , "Março" , "Abril" , "Maio" , "Junho" , "Julho" , "Agosto" , "Setembro" , "Outubro" , "Novembro" , "Dezembro")
print(tuplaMes)