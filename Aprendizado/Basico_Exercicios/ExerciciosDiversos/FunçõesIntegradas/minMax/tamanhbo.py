nomes = ["João Silva", "Ana Souza", "Carlos Montenegro"]
print(max(nomes,key=lambda n: len(n.split()[1])))