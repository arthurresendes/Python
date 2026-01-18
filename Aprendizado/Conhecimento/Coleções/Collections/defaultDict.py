"""
O defaultdict , são dicionarios que fornecem um valor padrão para chaves que não existem

Podemos usar o lambda para definir o valor padrão

Ela oferece uma funcionalidade útil para lidar com chaves inexistentes em um dicionário, fornecendo um valor padrão automaticamente quando uma chave não é encontrada.

"""
from collections import defaultdict as dd

# Recapitulando o dicionario
dicionario = {
    "curso": "Phyton"
}

print(dicionario)
print(dicionario['curso'])

# Criando um defaultdict com valor padrão de lista
dicionarioDefault = dd(lambda: 10)
dicionarioDefault['curso'] = 'Phyton'
print(dicionarioDefault)

# Aqui vemos que mesmo o outro não existindo, ele retorna o valor padrão definido pela lambda
print(dicionarioDefault['outro'])