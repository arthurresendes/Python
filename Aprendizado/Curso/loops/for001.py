"""

Estrutura de repetição

 

For (Para) em C e Java:

For (int i = 0 ; i < limitador ; i++){

    execução do loop

}

 

for item in interavel:

   //execução do loop

 

-String

   nome = 'Arthur'

-Lista

  lista = [1,2,3,4,5,6]

-Range

    numeros = rane(1,10)

"""

 

nome = 'Arthur Resende'

 

lista = [1,3,5,7,9]

 

numeros = range(1,11) # temos que transformar em uma lista

 

# Iterando sobre um nome

for letra in nome:

    print(letra)

 

print("\n")

 

# Iterando sobre uma lista

for numero in lista:

    print(numero)

 

print("\n")

 

# Iterando sobre um range

for num in numeros:

    print(num)

   

"""

Ou

for num in range(1,11):

    print(num)

"""
print("\n")

#range(inicio , fim , de quanto em quanto)

for teste in range(1,10,3):

    print(teste)

print("\n")

# Para o indice(posição começando em 0) e o valor(Valor do item em tal posição) in enumerate(objeto iterável que fornece pares com o índice e o valor)

for indice , letra in enumerate(nome):

    print(indice , letra)

print("\n")

for valor in enumerate(numeros):

    print(valor)

print("\n")


# Descartamos o indice e pegamos apenas o valor

for _, letra in enumerate(nome):

    print(letra)


print("\n")


for valor in enumerate(nome):

    print(valor)


nome = 'Arthur Resende'

for letra in nome:

    print(letra , end ='') #Tira o \n o end = ''


print('\n')

#U+1F60D - Emoji na unicode

#U0001F60D - Trocamos o + por tres zeros

#Usamos um \ antes do U para indicar que é um unicode

for x in range(3):
    for num in range(1 , 11):
       print('\U0001F60D' * num)


print('\n')

qtd =  int(input("Quantas vezes esse loop deve rodar: "))

soma = 0

for i in range(1,qtd + 1):

    number = float(input(f"Digite o valor de {i}/{qtd}: "))

    soma += number

print(f"Soma dos numeros no loop foi: {soma}")