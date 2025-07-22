from collections import deque as dq

fila = dq([1,2,3,4,5,6,7,8,9])

print(fila)
print("Chegou o numero 10 , ele eh preferencial")
fila.appendleft(10)
print(fila)