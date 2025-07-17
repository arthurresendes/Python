from collections import deque

fila = deque()
quantidadeValor = int(input("Quantos valores quer adicionar à fila: "))

for i in range(quantidadeValor):
    valor = int(input(f"Digite o valor do numero {i+1}: "))
    fila.append(valor)

for i in fila:
    print(i)

print("--Removendo elemento--")
print("Removido:", fila.popleft())  # Remove o primeiro

print("Fila atualizada")
filaOrdenada  = sorted(fila)

for i in filaOrdenada:
    print(i)