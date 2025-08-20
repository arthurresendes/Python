'''

with open('arquivo.txt', 'w') as file:
    pass

'''

import os

# Descobrindo se um arquivo ou diretorio existe

print(os.path.exists('arquivos.txt'))
print(os.path.exists('Aprendizado/Curso/Arquivo'))

#os.mknod('Aprendizado/Curso/Arquivos/teste.txt') -> Exemplo de criação de arquivo