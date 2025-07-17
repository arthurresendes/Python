class Pessoa:
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade

p = Pessoa("Arthur" , 19)
print("Nome:", p.nome, "Idade:", p.idade)