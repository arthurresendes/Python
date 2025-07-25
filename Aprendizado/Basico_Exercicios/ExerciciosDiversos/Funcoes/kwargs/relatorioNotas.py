def boletim(**kwargs):
    soma = 0
    for valor in kwargs.values():
        if isinstance(valor , int) or isinstance(valor , float):
            soma += valor
    media = soma/len(kwargs.keys())
    return f"Boletim: {kwargs}\nMédia geral: {media}"

print(boletim(matematica = 5 , portugues = 7 , ciencias = 8 , edFisica = 9))