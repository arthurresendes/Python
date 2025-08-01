x = int(input("Lado 1: "))

y = int(input("Lado 2: "))

z = int(input("Lado 3: "))

if x + y > z and x+z > y and y+z > x:
    print("Eh um triangulo!!")
    if x == y == z:
        print("E ele eh equilatero")
    elif x == y  or x == z or y == z:
        print("Eh isoceles")
    else:
        print("Escaleno")
else:
    print("Não eh um triangulo!!")