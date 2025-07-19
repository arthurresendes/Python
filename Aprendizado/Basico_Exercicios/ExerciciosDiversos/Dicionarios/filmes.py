filmes = {
    'Avengers': 9.5,
    'Superman': 10.0,
    'Quarteto Fantastico': 6.0
}
print("Todos os filmes: ")
print(filmes)
print("Maior nota: ")
print(filmes['Superman'])
print("Menor nota: ")
print(filmes.get('Quarteto Fantastico', 'Filme não foi encontrado'))
