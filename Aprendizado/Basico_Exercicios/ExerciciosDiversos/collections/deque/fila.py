from collections import deque as dq

fila = dq()
num = 0

for i in range(1,11):
    num = int(input("Digite um numero: "))
    fila.append(num)

print(fila)
print("Fila andando")
fila.popleft()
print(fila)

fila.rotate(2)
print(fila)