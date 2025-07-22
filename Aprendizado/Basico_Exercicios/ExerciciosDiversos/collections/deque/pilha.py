from collections import deque as dq

pilha = dq()
num = 0

for i in range(1,11):
    num = int(input("Digite um numero: "))
    pilha.append(num)

print(pilha)
print("Desimpilhando")
pilha.pop()
print(pilha)

print("Rotação")
pilha.rotate(2)
print(pilha)