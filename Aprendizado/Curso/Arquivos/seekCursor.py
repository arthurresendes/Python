'''

Seek e cursor

Seek -> Move o cursor para onde você quer

'''

import os


arquivo = r"C:\Users\arthu\OneDrive\Área de Trabalho\Programação\Projetos\Python\Aprendizado\Curso\Arquivos\arquivoSeek.txt"


arquivoEdita = r"C:\Users\arthu\OneDrive\Área de Trabalho\Programação\Projetos\Python\Aprendizado\Curso\Arquivos\arquivoedita.txt"


with open(arquivoEdita, 'w', encoding='UTF-8') as file:
    conteudo = file.write("Ola mundo")

with open(arquivoEdita, 'r', encoding='UTF-8') as file:

    conteudo = file.read()
    print(conteudo)

with open(arquivo, 'r', encoding='UTF-8') as file:
    # Pegando arquivos apos primeira linha
    file.seek(10)
    conteudo = file.read()
    print(list(conteudo.split()))

'''
try:
    arquivo3 = open('meu_arquivo.txt', 'w')
    arquivo3.write('Escrevendo no arquivo.')

finally:
    #arquivo.close() # Necessário fechar manualmente
# closed verifica se o arquivo esta aberto ou nao
'''