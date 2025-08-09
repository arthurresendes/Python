lista = []
soma = 0
for i in range(3):
    nota = float(input("Digite a nota: "))
    lista.append(nota)
for i in lista:
    soma += i
media = soma /3
print(media)
