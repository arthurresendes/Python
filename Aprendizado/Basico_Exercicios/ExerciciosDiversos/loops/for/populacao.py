contPessoas = 0
contFilhos = 0
contSalario100 = 0
somaSalario = 0.0
salarios = []

while True:
    print("Digite seu salario(0 para sair): ")
    salario = float(input(": "))
    if salario == 0.0:
        break
    else:
        salarios.append(salario)
    filhos = int(input("Quantos filhos tem: "))
    somaSalario += salario
    contFilhos += filhos
    contPessoas += 1
    if salario > 100.0:
        contSalario100 += 1

if contPessoas > 0:
    print(f"Total de pessoas: {contPessoas}")
    print(f"Media de filhos: {contFilhos/contPessoas}")
    print(f"Maior salario: {max(salarios)}")
    print(f"Percentual de pessoas com salario acima de 100: {(contSalario100 * 100)/contPessoas}")
else:
    print("Nenhum resultado disponivel")