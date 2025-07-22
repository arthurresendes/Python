from collections import namedtuple as nt

funcionario = nt("funcionario" , 'nome, salario')

nome = input("Digite o nome do funcionario: ")
salario = float(input(f"Digite o salario do {nome}: "))


testeSal = funcionario(nome,salario)

if testeSal.salario > 2999:
    print(f"Nome: {testeSal.nome}")
    print(f"Salario{testeSal.salario}" , sep=':') #Separador
else:
    print("So ira mostrar quem recebe mais de 3000")