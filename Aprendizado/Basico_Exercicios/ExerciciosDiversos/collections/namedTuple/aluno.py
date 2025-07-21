from collections import namedtuple as nt

Aluno = nt("Aluno", "nome idade nota")  # sem vírgula entre os campos
alunos = []

for i in range(3):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    idade = int(input(f"Digite a idade do aluno {i + 1}: "))
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    aluno = Aluno(nome, idade, nota)
    alunos.append(aluno)

print("\nDados dos alunos:")
for aluno in alunos:
    print(f"Nome: {aluno.nome} | Idade: {aluno.idade} | Nota: {aluno.nota}")
