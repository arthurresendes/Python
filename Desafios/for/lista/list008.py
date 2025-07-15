lista = ["maçã", "banana", "laranja"]
resultado = ""

for i in range(len(lista)):
    resultado += lista[i]
    if i < len(lista) - 1:
        resultado += ", "

print(f"Lista unida como string: {resultado}")
