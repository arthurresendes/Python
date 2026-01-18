import math

num = int(input("Digite um numero: "))

if num < 0 or num == 0:

    print("Numero invalido")

else:

    result = math.sqrt(num)

    print(f"A raiz quadrada de {num} eh {result}")