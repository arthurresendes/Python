pessoa = {"nome": "Arthur", "idade": 20, "cidade": "BH"}


dic_ite = iter(pessoa)

print(next(dic_ite))
print(next(dic_ite))
print(next(dic_ite))

for chave, valor in pessoa.items():
    print(chave, valor)