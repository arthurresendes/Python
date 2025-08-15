import os

arquivo = r"C:\Users\arthu\OneDrive\Área de Trabalho\Programação\Projetos\Python\Aprendizado\nomes.txt"

with open(arquivo, 'r') as file:
    conteudo = file.read()
    print(len(conteudo))
    file.seek(0)
    linhas =  file.readlines()
    print(len(linhas))