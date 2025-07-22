from collections import namedtuple as nt

Livro = nt("Livro" , 'nome, autor , ano')

nome = input("Digite o nome do livro: ")
autor = input("Digite o nome do autor: ")
ano = int(input("Digite o ano do livro: "))

livro1 = Livro(nome,autor,ano)

nome = input("Digite o nome do livro: ")
autor = input("Digite o nome do autor: ")
ano = int(input("Digite o ano do livro: "))

livro2 = Livro(nome,autor,ano)


print(f"Nome: {livro1.nome}")
print(f"Autor: {livro1.autor}")
print(f"Ano: {livro1.ano}")

if livro1.ano > 1999:
    print(f"Nome: {livro1.nome}")
    print(f"Autor: {livro1.autor}")
    print(f"Ano: {livro1.ano}")
if livro2.ano > 1999:
    print(f"Nome: {livro2.nome}")
    print(f"Autor: {livro2.autor}")
    print(f"Ano: {livro2.ano}")