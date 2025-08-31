'''
Aluno: com nome e idade.

Escola: que tem uma lista de alunos e métodos para:

adicionar aluno

listar alunos

👉 Use composição para armazenar objetos Aluno dentro da classe Escola.

'''


class Aluno:
    matricula = 0 
    def __init__(self , nome: str, idade: int):
        self.id = Aluno.matricula + 1
        self.nome = nome
        self.idade = idade
        Aluno.matricula = self.id

    def exibir_aluno(self):
        print(f"ID: {self.id} Nome: {self.nome} Idade: {self.idade}")

class Escola:
    def __init__(self):
        self.alunos = []
    
    def adicionar_alunos(self , aluno: Aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for i in self.alunos:
            i.exibir_aluno()

al1 = Aluno('Arthur' , 18)
esc = Escola()
esc.adicionar_alunos(al1)
esc.listar_alunos()