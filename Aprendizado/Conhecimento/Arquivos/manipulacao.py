'''

Modulo os é importante para a navegação / criação entre diretorios e arquivos alem de ter informações sobre o so do seu sistema


with open('arquivo.txt', 'w') as file:
    pass

'''

import os

# Descobrindo se um arquivo ou diretorio existe

print(os.path.exists('arquivos.txt'))
print(os.path.exists('Aprendizado/Curso/Arquivo'))

#os.mknod('Aprendizado/Curso/Arquivos/teste.txt') -> Exemplo de criação de arquivo

# os.rename('aquivoExistente', 'novoNome') -> Renomeando arquivos

# os.remove('nomearquivou')

'''
for arquivo os.scandir('oi'):
    if arquivo is file ():
        os.remove(arquivo)

'''

# os.removedirs('oi/mais') -> Removendo arvode de diretorios vazios