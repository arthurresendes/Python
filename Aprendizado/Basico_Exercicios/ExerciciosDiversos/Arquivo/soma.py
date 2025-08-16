arquivo = r"C:\Users\arthu\OneDrive\Área de Trabalho\Programação\Projetos\Python\Aprendizado\numeros.txt"


with open(arquivo , 'r',encoding='utf-8') as file:
    soma = 0
    for linha in file:
        soma += int(linha.strip())

print(soma)