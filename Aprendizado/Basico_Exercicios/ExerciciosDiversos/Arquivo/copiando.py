import os

arquivo = r"C:\Users\arthu\OneDrive\Área de Trabalho\Programação\Projetos\Python\Aprendizado\nomes.txt"
arquivo2 = r"C:\Users\arthu\OneDrive\Área de Trabalho\Programação\Projetos\Python\Aprendizado\copia.txt"


with open(arquivo, 'a+') as file:
    file.seek(0)  
    conteudo = file.read()

# Gravando no segundo arquivo
with open(arquivo2, 'w') as file:
    file.write(conteudo)

print("Arquivo copiado com sucesso!")
