'''
os - Sistema Operacional

'''

import os

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