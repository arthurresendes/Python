'''

O bloco with eh utilizado para criar um contexto de trabalho , onde os recursos utilizados são fechados apos o bloco with

 

with open(arquivo , modo , enconding) as apelido:

     conteudo = apelido.oque ira fazer

'''

 

import os

 

arquivo = r"C:\Users\arthu\OneDrive\Área de Trabalho\Programação\Projetos\Python\Aprendizado\Curso\Arquivos\arquivoedita.txt"


with open(arquivo , "w", encoding="UTF-8") as file:
    conteudo = file.write("Esse eh uma escrita em arquivos")

# Lendo oq foi escrito
with open(arquivo, "r", encoding="UTF-8") as file:
    print(file.read())