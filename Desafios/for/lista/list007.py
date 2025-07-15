lista = [2, 4, 2, 6, 2, 8, 4]
item = int(input("Digite o número que deseja contar na lista: "))
quantidade = 0

for valor in lista:
    if valor == item:
        quantidade += 1

print(f"O número {item} aparece {quantidade} vezes na lista.")
