nota = []
nome = []

for i in range(1,11):
    name = input(f"Digite o nome do aluno {i}: ")
    nome.append(name)
    note = int(input("Digite a nota do aluno: "))
    nota.append(note)

print(list(zip(nome,nota)))
print(f"Aluno com maior nota , tirou {max(nota)}")