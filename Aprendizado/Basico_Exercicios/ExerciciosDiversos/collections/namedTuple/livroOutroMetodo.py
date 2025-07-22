from collections import namedtuple as nt

# Definindo o namedtuple
Livro = nt("Livro", "nome autor ano")

# Função para cadastrar um livro
def cadastrar_livro():
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    ano = int(input("Digite o ano do livro: "))
    return Livro(nome, autor, ano)

# Cadastrando dois livros
livro1 = cadastrar_livro()
livro2 = cadastrar_livro()

# Lista para armazenar os livros
livros = [livro1, livro2]

# Exibindo os livros com ano > 1999
print("\nLivros publicados após 1999:")
for livro in livros:
    if livro.ano > 1999:
        print(f"\nNome: {livro.nome}")
        print(f"Autor: {livro.autor}")
        print(f"Ano: {livro.ano}")