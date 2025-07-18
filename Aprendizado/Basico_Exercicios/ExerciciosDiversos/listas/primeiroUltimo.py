lista = []

for i in range(6):
    cores = input(f"Digite a cor {i+1}: ")
    lista.append(cores)

print(lista[:1])
print(lista[-1:])