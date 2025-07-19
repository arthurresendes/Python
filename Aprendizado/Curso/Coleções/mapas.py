receita = {
    'jan': 100,
    'fev': 150,
    'mar': 200
}

print(receita)

# Iterando valores
print("\n")
for chave in receita:
    print(chave)
    

print("\n")
# Imprime o valor da chave
for chave in receita:
    print(receita[chave])
    

# Imprimindo chave e valor
print("\n")
for chave in receita:
    print(f"Em {chave} a receita foi: R$ {receita[chave]}")

print("\n")
# Dicionario de chaves
print(receita.keys())

print("\n")
for chave in receita.keys():
    print(chave)
    

print("\n")
# Acessando valores
print(receita.values())

for valor in receita.values():
    print(valor)
    
    
# Desempacotamendo 
print("\n")
print(receita.items())
for chave , valor in receita.items():
    print(f"Chave = {chave} e valor {valor}")


print("\n")
# Soma , maximo , minimo e tamanho
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))