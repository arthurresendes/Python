from collections import defaultdict

# Criando o defaultdict
nomes_por_letra = defaultdict(list)

# Lista de nomes
nomes = ["Alice", "André", "Bruna", "Bruno", "Caio", "Carlos"]

# Agrupando por letra inicial
for nome in nomes:
    inicial = nome[0].upper()  
    nomes_por_letra[inicial].append(nome)

# Exibindo os grupos
for letra, lista_nomes in nomes_por_letra.items():
    print(f"{letra}: {lista_nomes}")
