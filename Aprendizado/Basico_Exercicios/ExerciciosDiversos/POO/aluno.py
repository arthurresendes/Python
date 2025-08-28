class Aluno:
    def __init__(self,nome,idade,curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def exibir(self):
        return f"Nome {self.nome}\n Idade: {self.idade}\n Curso:{self.curso}"

aluno1 = Aluno("Arthur", 18, 'Python')
aluno2 = Aluno("Diego", 22, 'C')
aluno3 = Aluno("Davi", 17, 'SQL')

print(aluno1.exibir())
print(aluno2.exibir())
print(aluno3.exibir())

