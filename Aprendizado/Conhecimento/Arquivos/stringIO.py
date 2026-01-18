'''
StringIO - Utilizado para ler e criar arquivos em memoria

Para ler ou escrever dados em arquivos do sistema operacional , o software precisa ter permissão:
- Leitura de arquivo
- Escrita em arquivo
'''
from io import StringIO

mensagem = 'Olá mundo'
arquivo = StringIO(mensagem)

#Arquivo criado em memoria
print(arquivo.read())
arquivo.write("Mais um texto\n")
arquivo.seek(0)
print(arquivo.read())