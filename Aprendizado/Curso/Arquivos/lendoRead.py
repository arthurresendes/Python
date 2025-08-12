'''
Read em python

Para o conteudo de um arquivo utilizamos o open() 

open -> Na forma mais simples de utilização nos passamos apenas um parametro
'''
import os

arquivo = r"C:\Users\arthu\OneDrive\Área de Trabalho\Programação\Projetos\Python\Aprendizado\Curso\Arquivos\arquivo.txt"

arquivoLong = r"C:\Users\arthu\OneDrive\Área de Trabalho\Programação\Projetos\Python\Aprendizado\Curso\Arquivos\long.txt"

with open(arquivo, "r", encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)

with open(arquivoLong, 'r' , encoding='UTF-8') as file:
    conteudo2 = file.readline()
    print(conteudo2)