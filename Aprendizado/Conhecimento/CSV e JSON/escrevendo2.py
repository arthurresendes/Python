from csv import DictWriter

with open('filmes2.csv' 'w') as file:
    cabecalho = ['Titulo', 'Genero', 'Duração']
    escritor = DictWriter(file, fieldnames=cabecalho)
    escritor.writeheader()
    filme = None
    while filme != 'sair':
        filme = input("Informe o nome do filme(digite sair para sair): ")
        if filme != 'sair':
            genero = input("Informe o genero do filme: ")
            duracao = input("Informe a duração do filme em minutos: ")
            escritor.writerow({"Titulo": filme,"Genero": genero,"Duração": duracao})
        else:
            break