'''
os - Sistema Operacional

'''

import os
import sys

print(os.getcwd()) # Retorna onde o arquivo esta alocado

# Voltando diretorios
os.chdir('..')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())

# Checkagem se um diretorio é absoluto ou relativo

print(os.path.isabs('/Programacao/Python'))
print(os.path.isabs('C:\\Users\arthu'))

# Nome do so
print(os.name)

# Outro modo de ver
print(sys.platform)

# Listando diretorios
print(os.listdir('C://'))
arquivos = list(os.scandir())
scanner = os.scandir()
print("\n")
print(arquivos)
scanner.close()