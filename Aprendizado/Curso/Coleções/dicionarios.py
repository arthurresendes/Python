"""

Dicionarios são coleções do tipo chave/valor

Obs: Em algumas linguagens de programação são chamados de mapas ou tabelas hash

Dicionario são representados por {} , chaves e valor são separados por dois pontos (:) e os itens por virgula (,), podendo ser qualquer tipo de dados , podendo ter uma mescla de tipo de dados. Não podemos ter chaves repetidas

None é o valor nulo em py , utilizado para indicar que a variavel não possui um valor predefinido. None sempre é um valor falso

Iteravel é um objeto que pode ser percorrido
"""

print(type({}))

# 1 forma

print("Os dicionario são feitos por chave e seu devido valor. Segue exemplo: ")
paises = {'br': 'Brasil' , 'eua': 'Estados Unidos' , 'fr': 'França'}
print(paises)

# Acessando valores
print("Acessando valores: ")
print("1 forma(.get): ")
print(paises.get('br'))
print("2 forma: ")
print(paises['br'])
print("Com o .get é mais seguro ,pois se tiver algum engano não da erro e retorna None , já com [] da erro")
# Outro metodo de criar, nesse caso a chave parece uma variavel recebendo valor

paises2 = dict(br='Brasil' , eua="Estados Unidos" , fr="França")

# No get podemos passar o valor e depois colocar uma virgula caso não encontre coloque um valor padrão
pais = paises.get('ru' , 'País não encontrado')
print

"""
if pais:
    print(f"País encontrado {pais}")
else:
    print("País não encontrado")
"""
# Verificação 
print('br' in paises)
print('ru' in paises)


localidades = {
    (35.6895, 396917): "Escritorio Tokio",
    (32.6394, 323127): "Escritorio São Paulo",
    (25.1125, 334527): "Escritorio Nova York",
    (47.6895, 396917): "Escritorio Londres",
}

print(localidades)


receita = {
    'jan': 100,
    'fev': 200,
    'mar': 300
}

print(receita)

print("Adicionando valores: ")
receita['abr'] = 400
print(receita)

# Outro metodo
novoMes = {'mai': 500}
receita.update(novoMes)
print(receita)

# Atualizando valores
print("Atualizando dict: ")
receita['mai'] = 550
print("1 forma: ")
print(receita)
print("2 forma(update): ")
receita.update({'mai': 600})
print(receita)

# Removendo valores
print("Remoção: ")
#Obrigatorio passar a chave
retira = receita.pop('mar')
print(receita)
# 2 forma 
del receita['fev']
print(receita)

print("\n\n")
carrinho = []

produto1 = {
    'nome' : 'Plastation 5',
    'preco' : 5000,
    'quantidade' : 1
}

produto2 = {
    'nome' : 'God Of War',
    'quantidade': 1,
    'preco': 150
}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)


outro = {}.fromkeys('a', 'b')
print(outro)

# Todos valores serão desconhecidos
user = {}.fromkeys(['nome' , 'sobrenome', 'email,profile'] , 'desconhecido')

novo = {}.fromkeys(range(1,11),'desconhecido')
print(novo)