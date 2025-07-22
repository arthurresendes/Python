from collections import namedtuple as nt

Distancia = nt("Distancia" , 'x,y,distance')

x = int(input("Digite o numero de x: "))
y = int(input("Digite o numero de y: "))

d = abs(x - y)
resultado = Distancia(x,y,d)

print(f"X: {resultado.x}")
print(f"Y: {resultado.y}")
print(f"Distância: {resultado.distance}")