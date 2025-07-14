prova = int(input("Quantas provas você teve: "))
soma = 0
notas = []

for i in range(prova):
    num = float(input(f"Digite a nota da prova {i+1}: "))
    soma = soma + num
    notas.append(num) # O método .append() é usado para adicionar um item ao final de uma lista.

mediaA = soma / prova

for i in range(prova):
    print(f"Nota {i+1}: {notas[i]}")

print(f"A media das notas foram: {mediaA}")