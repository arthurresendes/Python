nome = input("Digite o seu nome: ").title().split(',')
mapeamento = map(lambda x: f"Ola {x.strip()}" , nome)
print(tuple(mapeamento))