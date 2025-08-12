import os 

arquivo = r"C:\Users\arthu\OneDrive\Área de Trabalho\Programação\Projetos\Python\Aprendizado\Basico_Exercicios\ExerciciosDiversos\Arquivo\leitura\texto.txt"

try:
    with open(arquivo, 'r' , encoding='UTF-8') as file:
        conteudo = file.read()
        print(conteudo)
except (FileExistsError,FileNotFoundError):
    print("Arquivo não encontrado")
