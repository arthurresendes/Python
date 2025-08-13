'''

Escrevendo em arquivos ("w")

 

Caso você escreva em um arqiuivo que ja tem um conteudo , ele ira sobrescrever e caso colocar o nome do arquivo e ele não existir ele ira ser criado

 

'''

 

import os

 

arquivo = r"C:\Users\arregomes\OneDrive - rd.com.br\Documentos\Python\Arquivos\escrita.txt"

 

with open(arquivo , "w", encoding='UTF-8') as file:

    file.write("Escrever dados em arquivos eh facil\n")

    file.write("Podemos colocar quantas linhas quisermos\n")

    file.write("Ultima linha")

 

# Se colocar um arquivo que não existe ele eh criado

with open('ola.txt' , "w", encoding='UTF-8') as file:

    file.write("Criando arquivo\n")

    file.write("Sem existir\n")

    file.write("Antes disso")




with open(arquivo , 'r', encoding='UTF-8') as file:

    print(file.read())

 

with open('ola.txt' , 'r', encoding='UTF-8') as file:

    print(file.read())

