# Entrada: índice

# Exiba valor correspondente ou "Índice fora da lista."

lista = [1, 2, 3, 4, 5]

try:
    indice = int(input("Digite o índice que quer ver da lista: "))
    print(f"Valor no índice {indice}: {lista[indice]}")

except IndexError:
    print("Índice fora da lista.")
except ValueError:
    print("Digite apenas números inteiros.")