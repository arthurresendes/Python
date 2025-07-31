nomes = ["Ana", "Carlos", "Lu", "Pedro", "Sol"]

result = list(map(lambda n : n.upper() , filter(lambda n : len(n) > 4, nomes)))
print(result)