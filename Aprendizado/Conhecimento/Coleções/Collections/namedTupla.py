"""

namedtuple é uma função que cria uma classe que herda de tuple, mas com campos nomeados que podem ser acessados como atributos. Ele combina a leveza e imutabilidade de uma tupla com a conveniência de acesso por nome de uma classe.

"""
from collections import namedtuple as nt
# Precisamos passar o nome da classe e os campos que ela terá
Cachorro = nt('Cachorro' , 'nome ,idade')
valor1 = input("Digite o nome do cachorro: ")
valor2 = int(input("Digite a idade do cachorro: "))
valores = Cachorro(valor1,valor2)

print(valores.nome)
print(valores.idade)
outraResposta = Cachorro(idade = 10 ,nome = 'Rex')
print(outraResposta[0])
print(outraResposta[1])