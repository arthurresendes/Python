qtd = int(input("Quantas idades quer adicionar: "))
idades = []
for i in range(qtd):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade)

print(f"Maior idade: {max(idades)}")
print(f"Menor idade: {min(idades)}")