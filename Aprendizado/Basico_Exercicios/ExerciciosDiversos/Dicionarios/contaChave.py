pessoa = {
    'nome': 'Arthur',
    'idade': 18
}

contador = 0

for chave in pessoa:
    if isinstance(pessoa[chave], int):
        print(f"Chave com valor inteiro: {chave}")
        contador += 1
        
print("Total de valores inteiros:", contador)
