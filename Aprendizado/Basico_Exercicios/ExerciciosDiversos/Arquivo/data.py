import time

arquivo = r"C:\Users\arthu\OneDrive\Área de Trabalho\Programação\Projetos\Python\Aprendizado\log.txt"

# Pega a data e hora atual de forma legível
inicio = time.strftime("%d/%m/%Y %H:%M:%S")

# Abre no modo append para não apagar dados antigos
with open(arquivo, 'a', encoding='utf-8') as file:
    file.write(f"Execução iniciada em: {inicio}\n")

print("Log registrado com sucesso!")
