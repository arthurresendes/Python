def dividir(a,b):
    if b == 0:
        raise ZeroDivisionError("Número não se divide por zero!")
    return a /b

num1 = int(input("Digite n1: "))
num2 = int(input("Digite n2: "))
print(dividir(num1,num2))