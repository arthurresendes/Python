def boletim(**kwargs):
    soma = 0
    total_notas = 0

    for valor in kwargs.values():
        if isinstance(valor, (int, float)):
            soma += valor
            total_notas += 1
        elif isinstance(valor, (list, tuple)):
            for nota in valor:
                if isinstance(nota, (int, float)):
                    soma += nota
                    total_notas += 1

    if total_notas == 0:
        return "Nenhuma nota válida informada."

    media = soma / total_notas
    return f"Boletim: {kwargs}\nMédia geral: {media:.2f}"

print(boletim(matematica = [4,9] , portugues = 7 , ciencias = 8 , edFisica = (9,10)))