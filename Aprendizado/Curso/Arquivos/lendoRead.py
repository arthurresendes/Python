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

# Readlines para muitas linhas
contador = 0
with open(arquivoLong, 'r' , encoding='UTF-8') as file:
    conteudo2 = file.readline()
    print(conteudo2)
    print(len(conteudo2)) # Conta quantas letras
    print(len(conteudo2.split())) # Conta quantas palavras
    for linhas in file:
        contador += 1
    print(contador)

# Metodo acima funciona assim no meu vscode , tendo que importar o os para localizar onde esta o arquivo txt, mas tem outro metodos que funcionam bem

try:
    arquivos = open("texto.txt")
    print(arquivos)
except (FileNotFoundError,FileExistsError):
    print("Não encontrado")
