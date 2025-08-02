nomes = ["João Silva", "Ana Souza", "Carlos Mendes"]
# Ordene pela segunda palavra (sobrenome).

print(sorted(nomes, key=lambda n: n.split()[1]))