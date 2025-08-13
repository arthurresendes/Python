import os

arquivo = r"C:\Users\arthu\OneDrive\Área de Trabalho\Programação\Projetos\Python\Aprendizado\Basico_Exercicios\ExerciciosCurso\Arquivo\arq.txt"

with open(arquivo , 'w', encoding="UTF-8") as file:
    while True:
        digitacao = input("Digite um documento ou 0 para sair: ")
        if digitacao == '0':
            break
        else:
            file.write(digitacao)

with open(arquivo , 'r', encoding='UTF-8') as file:
    print(file.read())